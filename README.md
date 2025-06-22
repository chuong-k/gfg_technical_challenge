# GFG Technical Challenge
This project is a technical assignment for a data engineering role. It utilizes **PySpark**, **Docker**, and **DuckDB** to build an ETL pipeline for transforming and loading data.

---
&nbsp;
## Table of Contents

- [Overview](#overview)
- [Technologies Used](#technologies-used)
- [Setup](#setup)
- [How to Run](#how-to-run)
- [Output](#output)
- [Notes](#notes)
- [Author](#author)

&nbsp;
## Overview

The goal of this project is to:
- Initialize a local Spark environment using Docker.
- Read input CSV data using PySpark.
- Perform transformations
- Load the transformed data into a database for Analysis work.

The pipeline is designed to be simple, modular, and reproducible for technical demonstration purposes.

&nbsp;
## Technologies Used

- **Python**
- **Apache Spark (PySpark)**
- **DuckDB** + **DuckDB CLI/UI** 
- **Docker & Docker Compose**

&nbsp;
## Setup

> Prerequisites:
- Install [Docker](https://www.docker.com/)
- Install [DuckDB CLI/UI](https://duckdb.org/docs/installation/)

&nbsp;
## How to Run

1. git clone git@github.com:chuong-k/gfg_technical_challenge.git\
& cd gfg_technical_challenge

&nbsp;

2. Start Docker services  `docker compose up --build -d --scale spark-worker=2`

&nbsp;

3. Execute command to extract zip file  `docker exec spark-master bash /opt/spark/work-dir/entrypoint.sh`

&nbsp;

4. Running a Jupyter Notebook (Optional)
```bash
docker exec spark-master bash -c "jupyter notebook --ip=0.0.0.0 --port=3000 --allow-root"
```
Take the last URL printed out in the console log and pasted it over to your browser and the Notebook will open up
<img width="1440" alt="Image" src="https://github.com/user-attachments/assets/b622803c-594c-4210-825d-e544c3c8cfec" class="center"/>

&nbsp;

5. Execute the ETL script
```bash
docker exec -w  /opt/spark/work-dir/gfg_technical_challenge/etl spark-master spark-submit main.py
```

&nbsp;
## Output

A DB object file will appear in `gfg_technical_challenge/db`, which can be seen in both Jupyter or in the project repo via your favorite IDE.

<img width="1440" alt="Image" src="https://github.com/user-attachments/assets/4a1f123f-b022-47c5-bec8-08de98511c87" />

