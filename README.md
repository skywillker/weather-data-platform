# Weather Data Platform

## Project Status
🟢 Current Version: Sprint 2A completed

The project is being developed incrementally through planned sprints.

See `docs/Roadmap.md` for the complete roadmap.

## Introduction

A Data Engineering project that incrementally builds a production-inspired weather data platform using public meteorological data.

## Context

This project was created to demonstrate an incremental construction of a data platform, following engineering practices commonly adopted in production environments.

## Current Features

- Retrieve weather data from the Open-Meteo API
- Store raw responses as JSON files
- Organize the project using a modular Python structure

## Architecture 

```text
Open-Meteo API
        │
        ▼
Python Ingestion Script
        │
        ▼
JSON Files
```

## Getting Started

1. Clone the repository

2. Install the dependencies

```bash
pip install -r requirements.txt
```

3. Run the ingestion script

```bash
python -m src.ingestion.weather_api
```

## Documentation

Additional documentation is available in the `docs/` directory:

- Architecture
- Roadmap
- Changelog
- Architecture Decision Records (ADRs)

## Cost

Current version: Free

The project uses only free tools and public weather data.