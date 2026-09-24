## Project Overview

An end-to-end data engineering pipeline that extracts port operations data from multiple heterogeneous sources using Python. 
Raw source data is archived in AWS S3 and loaded into PostgreSQL, where dbt models transform and validate the data into analytics-ready staging models and performance marts.

The entire environment is containerized with Docker and Docker Compose, while Apache Airflow orchestrates the ingestion, transformation, and data-quality testing workflow.


## Architecture

The pipeline integrates three different source types:

- **REST API** — vessel call and schedule data
- **CSV files** — container movement events
- **PostgreSQL** — berth operation records

Python ingestion jobs extract data from each source and archive the raw data in **AWS S3**. 
The archived data is then loaded into the `raw` schema of the analytical PostgreSQL database using idempotent loading strategies.

**dbt** transforms the raw data into cleaned staging models and analytical marts for vessel, berth, and terminal performance. dbt tests validate data quality and business consistency.

The complete workflow is orchestrated by **Apache Airflow**:

`ingestion → dbt run → dbt test`


## Business Goal

The pipeline generates analytical datasets for monitoring key areas of port operations:

- **Vessel performance** — cargo operation metrics, operational delays, and potential schedule overruns.
- **Berth performance** — number of vessels handled, berth utilization time, and total cargo throughput.
- **Terminal performance** — number of vessel calls, cargo operation time, and total cargo handled by each terminal.

These analytical marts combine data from multiple operational sources into a consistent structure that can be used for operational analysis, reporting, and further visualization.


## Technology Stack

- **Python** — data extraction, ingestion, S3 integration, and loading data into the warehouse.
- **AWS S3** — raw data storage and historical archive for data extracted from source systems.
- **PostgreSQL** — source operational database and analytical data warehouse.
- **dbt** — SQL-based data transformation, staging models, analytical marts, and data-quality testing.
- **Docker & Docker Compose** — containerization and management of the pipeline services and development environment.
- **Apache Airflow** — workflow orchestration, scheduling, and execution of ingestion, dbt transformations, and tests.


## Data Sources

The project uses simulated port-operation data generated locally to represent three different types of real-world source systems:

- **Vessel Calls API** — a locally hosted REST API providing vessel schedules, arrival/departure times, terminal and berth assignments, vessel status, and update timestamps. API responses are archived in AWS S3 as JSON.
- **Container Movement Files** — generated CSV files representing individual container loading and discharge events, including vessel call, crane, container size, weight, and event time. Original CSV files are archived in S3 before processing.
- **Berth Operations Database** — a separate PostgreSQL database simulating an operational source system containing planned and actual berth-operation times, operation status, berth assignments, and update timestamps. Extracted snapshots are archived in S3 as Parquet.

All three sources share operational identifiers such as `vessel_call_id`, allowing the datasets to be integrated during transformation.


## Data Flow and Ingestion Strategy

Each source follows a source-specific ingestion strategy while using AWS S3 as the common raw landing and archival layer.

**Vessel Calls API:** Vessel data is extracted from the REST API and archived in S3 as JSON. The data is then read from S3 and upserted into the PostgreSQL `raw.vessel_raw` table. Existing vessel calls are updated only when the incoming record has a newer `updated_at` timestamp.

**Container Movements:** Incoming CSV files are archived in S3 before being loaded into `raw.cargo_ops_raw`. The original file is moved from the `incoming` directory to `processed` only after the warehouse load succeeds, allowing failed loads to be retried. Duplicate movement records are prevented using the unique `move_id`.

**Berth Operations:** The operational PostgreSQL source table is extracted as a full snapshot and archived in S3 as Parquet. The snapshot is then loaded into `raw.berth_ops_raw`, where `operation_id` identifies individual operations and newer versions are applied according to `updated_at`.

After ingestion, dbt transforms the three raw datasets through the staging layer and produces analytical marts for vessel, berth, and terminal performance.


## dbt Transformation Layer

dbt is used to transform raw operational data into clean, analytics-ready datasets.

The transformation layer follows a simple three-stage structure:

`raw → staging → marts`

The **raw layer** contains data loaded from the source systems. 
The **staging layer** cleans and standardizes source fields, applies consistent naming and status values, and prepares the datasets for downstream joins and aggregations.
The **mart layer** produces business-level analytical models:

- `mart_vessel_performance` — vessel-level operational and cargo performance.
- `mart_berth_performance` — berth-level vessel activity, operating time, and cargo throughput.
- `mart_terminal_performance` — terminal-level vessel calls, operating time, and cargo throughput.

Cargo and berth data are aggregated to the appropriate grain before joining where necessary, preventing incorrect results caused by many-to-many joins.


## Data Quality and Reliability

The pipeline includes several mechanisms to make ingestion repeatable and protect data quality:

- **Idempotent loading** — rerunning the pipeline does not create duplicate source records.
- **Conflict handling** — vessel calls and berth operations are updated only when incoming records contain a newer `updated_at` timestamp.
- **Duplicate prevention** — cargo movements use `move_id` as a unique event identifier and ignore already-loaded events.
- **Safe file processing** — incoming CSV files are moved to the `processed` directory only after a successful warehouse load.
- **dbt schema tests** — uniqueness, `not_null`, and relationship constraints validate key fields and relationships between datasets.
- **Business-rule tests** — custom dbt tests validate operational consistency, including berth-operation timing, completion/progress states, overruns, cargo movements, and analytical mart results.
- **Raw data preservation** — source data is archived in timestamped S3 objects before warehouse processing, preserving the original ingestion history.

The complete Airflow DAG was also tested through repeated executions to verify that successful reruns produce consistent warehouse results without duplicate records.


## Workflow Orchestration

Apache Airflow orchestrates the complete pipeline as a three-step DAG:

`ingestion → dbt_run → dbt_test`

- **`ingestion`** — executes the Python ingestion pipeline, extracting source data, archiving it in S3, and loading it into the PostgreSQL raw layer.
- **`dbt_run`** — builds the dbt staging models and analytical marts.
- **`dbt_test`** — runs dbt data-quality and business-rule tests after successful transformation.

Each downstream task runs only after the previous stage completes successfully.