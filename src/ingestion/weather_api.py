import requests
from src.config.settings import (
    API_BASE_URL,
    API_PARAMS,
    REQUEST_TIMEOUT,
)
from src.config.logging_config import logger
from src.storage.bronze import save

def fetch_weather():
    """
    Fetch current weather data from Open-Meteo API.
    """
    logger.info("Initiating weather data ingestion.")
    
    try:
        response = requests.get(
            API_BASE_URL,
            params=API_PARAMS,
            timeout=REQUEST_TIMEOUT,
        )

        response.raise_for_status()

    except requests.RequestException:
        logger.exception("Failed to fetch weather data.")
        raise

    return response.json()


if __name__ == "__main__":
    data = fetch_weather()

    save(
        domain="weather",
        dataset="current_weather",
        source="open_meteo",
        data=data,
    )

    logger.info("Ingestion completed.")