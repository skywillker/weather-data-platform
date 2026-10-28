# Silver Data Contract

## Purpose

The Silver Layer stores data transformed from the Bronze Layer into a standardized and analytics-ready structure.

## Grain

One row represents one weather observation for a specific location and observation timestamp.

## Format

Parquet.

## Silver Layer Responsibilities

* Transform Bronze records into the defined Silver schema;
* Clean and standardize data according to the defined data-quality rules;
* Standardize data types;
* Normalize observation timestamps to UTC;
* Represent missing source values as `NULL`;
* Validate defined structural and data-quality constraints;
* Remove logical duplicate observations;
* Apply the defined Hive partitioning pattern;
* Persist data as immutable Parquet files.

## The Silver Layer does not

* Preserve the raw source data completely;
* Enrich records with external data;
* Aggregate data;
* Replace missing values with arbitrary values;
* Modify data already persisted.

## Schema

| Column                     | Type        | Nullable | Description                                    |
| -------------------------- | ----------- | -------- | ---------------------------------------------- |
| `observation_timestamp`    | `timestamp` | No       | Weather observation timestamp in UTC           |
| `ingestion_timestamp`      | `timestamp` | No       | Timestamp when the record was ingested, in UTC |
| `latitude`                 | `double`    | No       | Observation latitude                           |
| `longitude`                | `double`    | No       | Observation longitude                          |
| `elevation_m`              | `double`    | Yes      | Elevation in meters                            |
| `temperature_2m_c`         | `double`    | Yes      | Temperature at 2 meters in Celsius             |
| `wind_speed_10m_kmh`       | `double`    | Yes      | Wind speed at 10 meters in km/h                |
| `observation_interval_sec` | `integer`   | Yes      | Observation interval in seconds                |
| `timezone`                 | `string`    | No       | Source timezone                                |
| `source`                   | `string`    | No       | Data source                                    |
| `dataset`                  | `string`    | No       | Source dataset                                 |
| `year`                     | `string`    | No       | Partition column                               |
| `month`                    | `string`    | No       | Partition column                               |
| `day`                      | `string`    | No       | Partition column                               |

## Partitioning

Silver data is partitioned by observation date using the following Hive-style pattern:

`year=YYYY/month=MM/day=DD`

The partitioning date is derived from `observation_timestamp`, not `ingestion_timestamp`.

## Deduplication

Logical duplicates are identified by:

`source + latitude + longitude + observation_timestamp`

When multiple records represent the same logical observation, the record with the latest `ingestion_timestamp` is retained.

## Expectations for Consumers

* All records conform to the defined Silver schema;
* Column names and data types follow the Silver contract;
* Consumers can rely on the defined structural and data-quality validations;
* Missing source values are represented as `NULL`;
* Logical duplicate observations are removed according to the defined deduplication rules;
* Observation timestamps are represented in UTC;
* Data is partitioned according to the defined Hive partitioning pattern;
* Raw source data should be accessed from the Bronze Layer when complete source fidelity is required.
