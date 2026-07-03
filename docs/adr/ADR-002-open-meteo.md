# ADR-002 - Centralized Logging Configuration

## Status

Accepted

## Context

The project relied on print() statements to provide execution feedback.

As the application grows, multiple modules will need a consistent mechanism to record execution events.

Using print() does not provide configurable log levels, multiple output destinations, or centralized configuration.

## Decision

Adopt a centralized logging configuration in src/config/logging_config.py.

All project modules must use the shared logger instead of calling print() directly.

## Rationale

- Single logging configuration for the entire application.
- Consistent log format.
- Support for multiple output destinations.
- Easy integration with future components such as Docker and Airflow.
- Separation between application logic and logging configuration.

## Consequences

Positive:

- Standardized logs.
- Easier debugging.
- Better maintainability.
- Reusable across future modules.

Negative:

- Slightly more complex initialization.
- Developers must use the shared logger instead of print().