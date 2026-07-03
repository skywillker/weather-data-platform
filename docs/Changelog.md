v0.1.1

Added

- Configuration module (`src/config/settings.py`)
- Centralized API request parameters
- Request timeout configuration
- Package structure using `__init__.py`
- Module execution with `python -m`

Changed

- Refactored weather ingestion to use `requests.get(..., params=...)`
- Removed hardcoded API URL construction