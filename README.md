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

1. `git clone git@github.com:chuong-k/gfg_technical_challenge.git & cd gfg_technical_challenge`

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

- A DB object file will appear in `gfg_technical_challenge/db`, which can be seen in both Jupyter or in the project repo via your favorite IDE.

<img width="1440" alt="Image" src="https://github.com/user-attachments/assets/4a1f123f-b022-47c5-bec8-08de98511c87" />

&nbsp;

- Follow the instruction of [DuckDB CLI](https://duckdb.org/docs/installation/) to install. We will use this to view the data.

&nbsp;

- Once done, in your terminal, execute below commands to connect to DuckDB.
```bash
cd gfg_technical_challenge
duckdb db/analysis.duckdb
```
<img width="1440" alt="Image" src="https://github.com/user-attachments/assets/3714d2c9-8d25-46a2-809c-2d2c55550b9d" />

&nbsp;

- Alternatively, installing DuckDB CLI also give user access to a sleek GUI to perform data exploration [DuckDB GUI](https://duckdb.org/2025/03/12/duckdb-ui.html#introducing-the-duckdb-ui)
&nbsp;
```bash
 duckdb -ui
```
<img width="1440" alt="Image" src="https://github.com/user-attachments/assets/39756daa-32ec-49cc-90cc-2d648bbf074d" />


&nbsp;
## Notes
**Why Spark?**\
Spark should not be too alien with people in the data scene. 
1. It is a hardened, battle-tested framework that has served many data stacks in many different orgs.
2. Designed for distributed computing, making it scale more easily. 
3. Powerful and flexible API, ideal to handle complex requirement for data - transform, filter, aggregation
4. Integration with other eco-system easily (HDFS, Databases, Files, etc...)

Although it is much overkill for this assignment.

&nbsp;

**Why DuckDB?**\
DuckDB is a new, modern tool for data analytic works
1. DuckDB is lightweight and easy to setup and use. It is perfect for local deployment
2. Support for Parquet file out of the box. Very good for Spark integration
3. Offer both connection and DB object file access mode

The core of most modern usually require a heavy-weight SQL tools for data exploration such as PostGreDB or Hive. DuckDB offers an alternative way to validate and analyze data in a fast, compact and friend way.


&nbsp;
## Author
Kiet Chuong

- GitHub: @chuong-k (Lost access to my old account)
- LinkedIn: linkedin.com/in/kietchuong

