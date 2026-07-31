# Bronze Data Contract 

## Purpose

The Bronze Layer stores raw data exactly as received from external sources while adding operational metadata required by the platform.

## Bronze Layer Responsibilities

- Every file includes metadata.
- Make sure that all files contain payload.
- Payload is completely preserved. 
- Ingestion timestamp in UTC. 
- Hive partitioning pattern. 
- Files are never modified after persisted.

## The Bronze Layer does not:

- clean data;
- remove duplicates;
- validate business rules;
- standardize schemas;
- enrich records;
- aggregate data.

## Expectations for consumers

- Envelope's contract will be respected. 
- All files have the same external structure. 
- New metadata fields may be added in a backward-compatible way.
- Consumers must not assume a fixed payload schema.
- Consumers must expect raw data quality issues.
- There might be duplicates. 