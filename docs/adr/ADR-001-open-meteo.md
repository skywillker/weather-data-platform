# ADR-001 - Choice of Weather Data Provider

## Status

Accepted

## Context

The project requires a free and publicly available weather data source to support the development of a complete data engineering platform.

## Alternatives

- OpenWeather
- INMET
- NOAA

## Decision

Open-Meteo was selected.

## Rationale

- Free
- No authentication required
- Easy to reproduce
- Well documented
- Simple REST API

## Consequences

Positive:

- Easy for anyone to reproduce the project.

Negative:

- Dependency on an external provider.
- API availability is outside our control.