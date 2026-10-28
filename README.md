# Weather Data Platform

## Project Status
🟢 Current Version: Sprint 5 completed

The project is being developed incrementally through planned sprints.

See `docs/Roadmap.md` for the complete roadmap.

## Introduction

A Data Engineering project that incrementally builds a production-inspired weather data platform using public meteorological data.

## Context

This project was created to demonstrate an incremental construction of a data platform, following engineering practices commonly adopted in production environments.

## Current Features

- Retrieve weather data from the Open-Meteo API.
- Store raw responses as timestamped JSON files.
- Centralized application configuration.
- Structured logging.
- Console and file logging.
- Dockerized application for reproducible execution.
- Modular project organization.
- Medallion Architecture started, with the Bronze and Silver Layers and their contract. 

## Current Limitations

- The Silver pipeline currently reads a specific Bronze date partition rather than processing the entire available Bronze history.
- Automated regression tests for Silver transformations and data-quality rules have not yet been implemented.

These limitations are intentional at the current development stage and will be addressed incrementally in upcoming sprints.

## Architecture 

```text
Open-Meteo API
        │
        ▼
Ingestion Layer
        │
        ▼
Bronze Layer
        │
        ▼
Silver Layer
        │
        ▼
Partitioned Parquet Dataset
```

## Getting Started

1. Clone the repository.

2. Build the Docker image.

```bash
docker build -t weather-data-platform .
```

3. Run the container. 
```bash
docker run --rm \
-v "$(pwd)/data:/app/data" \
weather-data-platform
```

## Documentation

Additional documentation is available in the `docs/` directory:

- Architecture
- Roadmap
- Changelog
- Architecture Decision Records (ADRs)
- Contracts

## Cost

Current version: Free

The project uses only free tools and public weather data.