import logging
from pathlib import Path

LOG_FORMATTER = logging.Formatter(
    "%(asctime)s | %(levelname)s | %(message)s"
)

PROJECT_ROOT = Path(__file__).resolve().parents[2]
LOGS_DIR = PROJECT_ROOT / "logs"

LOGS_DIR.mkdir(parents=True, exist_ok=True)

LOG_FILE = LOGS_DIR / "weather_platform.log"

file_handler = logging.FileHandler(LOG_FILE, encoding="utf-8")
console_handler = logging.StreamHandler()

file_handler.setFormatter(LOG_FORMATTER)
console_handler.setFormatter(LOG_FORMATTER)

logger = logging.getLogger("weather_platform")
logger.setLevel(logging.INFO)

if not logger.handlers:
    logger.addHandler(file_handler)
    logger.addHandler(console_handler)