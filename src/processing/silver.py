from pyspark.sql import DataFrame, SparkSession
from pyspark.sql import functions as F
from pyspark.sql import Window


def create_spark_session() -> SparkSession:
    """Create and configure the Spark session for the Silver pipeline."""
    return (
        SparkSession.builder
        .appName("weather-data-platform-silver")
        .master("local[*]")
        .config("spark.sql.session.timeZone", "UTC")
        .getOrCreate()
    )


def read_bronze(spark: SparkSession, input_path: str) -> DataFrame:
    """Read Bronze JSON data into a Spark DataFrame."""
    return spark.read.json(input_path, multiLine=True)


def flatten_bronze(df: DataFrame) -> DataFrame:
    """Project nested Bronze fields into a tabular Silver structure."""
    return df.select(
        F.col("metadata.ingestion_timestamp").alias("ingestion_timestamp"),
        F.col("payload.latitude").alias("latitude"),
        F.col("payload.longitude").alias("longitude"),
        F.col("payload.elevation").alias("elevation_m"),
        F.col("payload.current.time").alias("observation_time"),
        F.col("payload.current.interval").alias("observation_interval_sec"),
        F.col("payload.current.temperature_2m").alias("temperature_2m_c"),
        F.col("payload.current.wind_speed_10m").alias("wind_speed_10m_kmh"),
        F.col("payload.timezone").alias("timezone"),
        F.col("metadata.source").alias("source"),
        F.col("metadata.dataset").alias("dataset"),
    )

def standardize_types(df: DataFrame) -> DataFrame:
    """Standardize Silver column names, types, and timestamps."""
    return df.select(
        F.to_utc_timestamp(
            F.to_timestamp(
                "observation_time",
                "yyyy-MM-dd'T'HH:mm"
            ),
            F.col("timezone")
        ).alias("observation_timestamp"),
        F.to_timestamp("ingestion_timestamp")
        .alias("ingestion_timestamp"),
        F.col("latitude").cast("double").alias("latitude"),
        F.col("longitude").cast("double").alias("longitude"),
        F.col("elevation_m").cast("double").alias("elevation_m"),
        F.col("temperature_2m_c").cast("double").alias("temperature_2m_c"),
        F.col("wind_speed_10m_kmh").cast("double").alias("wind_speed_10m_kmh"),
        F.col("observation_interval_sec").cast("integer")
        .alias("observation_interval_sec"),
        F.col("timezone").cast("string").alias("timezone"),
        F.col("source").cast("string").alias("source"),
        F.col("dataset").cast("string").alias("dataset"),
    )

def deduplicate_observations(df: DataFrame) -> DataFrame:
    """Keep the latest ingestion for each weather observation."""

    window = (
        Window
        .partitionBy(
            "source",
            "latitude",
            "longitude",
            "observation_timestamp",
        )
        .orderBy(F.col("ingestion_timestamp").desc())
    )

    return (
        df.withColumn(
            "_row_number",
            F.row_number().over(window),
        )
        .filter(F.col("_row_number") == 1)
        .drop("_row_number")
    )


def validate_silver(df: DataFrame) -> None:
    """Fail if any required Silver field is null."""

    required_columns = [
        "observation_timestamp",
        "ingestion_timestamp",
        "latitude",
        "longitude",
        "timezone",
        "source",
        "dataset",
    ]

    invalid_condition = F.lit(False)

    for column in required_columns:
        invalid_condition = invalid_condition | F.col(column).isNull()

    invalid_count = df.filter(invalid_condition).count()

    if invalid_count > 0:
        raise ValueError(
            f"Silver contract validation failed: "
            f"{invalid_count} row(s) have null required fields."
        )

def add_partition_columns(df: DataFrame) -> DataFrame:
    """Add zero-padded Hive partition columns from observation timestamp."""

    return (
        df
        .withColumn(
            "year",
            F.year("observation_timestamp").cast("string"),
        )
        .withColumn(
            "month",
            F.lpad(F.month("observation_timestamp").cast("string"), 2, "0"),
        )
        .withColumn(
            "day",
            F.lpad(F.dayofmonth("observation_timestamp").cast("string"), 2, "0"),
        )
    )


def write_silver(df: DataFrame, output_path: str) -> None:
    """Persist Silver data as partitioned Parquet files."""

    (
        df.write
        .partitionBy("year", "month", "day")
        .parquet(output_path)
    )


def main() -> None:
    spark = create_spark_session()

    try:
        bronze_df = read_bronze(
            spark,
            "data/bronze/weather/current_weather/open_meteo/year=2026/month=07/day=31",
        )

        flattened_df = flatten_bronze(bronze_df)

        standardized_df = standardize_types(flattened_df)

        silver_df = deduplicate_observations(standardized_df)

        validate_silver(silver_df)

        silver_df = add_partition_columns(silver_df)

        silver_df.printSchema()
        silver_df.show(truncate=False)

        write_silver(
            silver_df,
            "data/silver/weather/current_weather",
        )

    finally:
        spark.stop()


if __name__ == "__main__":
    main()