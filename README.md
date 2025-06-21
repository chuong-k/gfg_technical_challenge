# GFG Technical Challenge
This project is a technical assignment completed for a data engineering role. It demonstrates the use of **PySpark**, **Docker**, and **PostgreSQL** to build an end-to-end ETL pipeline for transforming and loading transaction data.

---

## Table of Contents

- [Overview](#overview)
- [Technologies Used](#technologies-used)
- [Setup Instructions](#setup-instructions)
- [How to Run](#how-to-run)
- [Output](#output)
- [Notes](#notes)
- [Author](#author)

---

## Overview

The goal of this project is to:
- Initialize a local Spark environment using Docker.
- Read input CSV data using PySpark.
- Perform a series of transformations (e.g., filtering, joins, and aggregations).
- Save the results as a **partitioned Parquet file**.
- Load the transformed data into a **PostgreSQL** database.

The pipeline is designed to be simple, modular, and reproducible for technical demonstration purposes.

---

## Technologies
 
- **Python**
- **Apache Spark (PySpark)**
- **Docker & Docker Compose**

---

## Setup Instructions

> Prerequisites: Install [Docker](https://www.docker.com/)

1. Clone the repository:
```bash
git clone https://github.com/chuong-k/gfg_technical_challenge.git
cd gfg_technical_challenge
```

2. Start Docker services
```bash
docker compose up --build -d
```

3. Execute command to extract zip file
```bash
docker exec spark-master bash /opt/spark/work-dir/entrypoint.sh
```
This will unzip the zip file placed under /data/zip_data/test_data.zip. This file was acquired from GFG technical assessment repository https://github.com/theiconic/technical-challenges

4. Running a Jupyter Notebook (Optional)
```bash
docker exec spark-master bash -c "jupyter notebook --ip=0.0.0.0 --port=3000 --allow-root"
```

5. Execute the ETL script. This step will take a while to download Spark related package from central repository, please do not cancel until output has been generated.
```bash
docker exec -w  /opt/spark/work-dir/gfg_technical_challenge/ spark-master spark-submit main.py
```
