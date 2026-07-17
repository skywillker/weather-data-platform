                    Docker Container
                           │
                           ▼
                  weather_api.py
             ┌────────────┼────────────┐
             ▼            ▼            ▼
      settings.py   logging_config.py  Open-Meteo API
             │                         │
             └────────────┬────────────┘
                          ▼
                  data/raw/*.json