                    Configuration Layer
        ┌────────────────────┴────────────────────┐
        ▼                                         ▼
 settings.py                           logging_config.py
        │                                         │
        └────────────────────┬────────────────────┘
                             ▼
                    weather_api.py
                    ┌────────┴────────┐
                    ▼                 ▼
            Open-Meteo API      Logging System
                    │           ┌──────┴──────┐
                    ▼           ▼             ▼
           data/raw/*.json  Console      logs/*.log