from pathlib import Path

PROJECT_ROOT = Path(__file__).resolve().parents[2]
DATA_DIR = PROJECT_ROOT / "data"

API_BASE_URL = "https://api.open-meteo.com/v1/forecast"

API_PARAMS = {
    "latitude": -23.5750,
    "longitude": -46.5700,
    "timezone": "America/Sao_Paulo",
    "current": [
        "temperature_2m",
        "wind_speed_10m",
    ],
}

REQUEST_TIMEOUT = 10
