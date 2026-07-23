from datetime import datetime, timezone
from pathlib import Path
import json

from src.config.logging_config import logger
from src.config.settings import DATA_DIR


def save(
    domain: str,
    dataset: str,
    source: str,
    data: dict,
) -> None:
    """
    Save raw data into the Bronze layer.
    """

    timestamp = datetime.now(timezone.utc)

    output_dir = (
        DATA_DIR
        / "bronze"
        / domain
        / dataset
        / source
        / f"year={timestamp:%Y}"
        / f"month={timestamp:%m}"
        / f"day={timestamp:%d}"
    )

    output_dir.mkdir(
        parents=True,
        exist_ok=True,
    )

    filename = f"{domain}_{timestamp:%Y%m%dT%H%M%SZ}.json"

    output_file = output_dir / filename

    with open(output_file, "w", encoding="utf-8") as file:
        json.dump(
            data,
            file,
            indent=4,
            ensure_ascii=False,
        )

    logger.info("Data saved to Bronze layer: %s", output_file)