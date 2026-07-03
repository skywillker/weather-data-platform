from pathlib import Path
import requests
import json
from datetime import datetime
from src.config.settings import (
    API_BASE_URL,
    API_PARAMS,
    REQUEST_TIMEOUT,
)


def fetch_weather():
    """
    Fetch current weather data from Open-Meteo API.
    """
    response = requests.get(
        API_BASE_URL,
        params=API_PARAMS,
        timeout=REQUEST_TIMEOUT,
)
    response.raise_for_status()

    return response.json()


def save_json(data):
    timestamp = datetime.now().strftime("%Y-%m-%d_%H-%M-%S")

    base_dir = Path(__file__).resolve().parents[2]

    output_file = base_dir / "data" / "raw" / f"weather_vp_{timestamp}.json"

    with open(output_file, "w", encoding="utf-8") as f:
        json.dump(data, f, indent=4, ensure_ascii=False)

    print("Data saved in:", output_file)


if __name__ == "__main__":
    data = fetch_weather()
    save_json(data)