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
- [Task](#task)
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

## Task

Follow-up on Task in [GFG Repo](https://github.com/theiconic/technical-challenges/tree/master/data/data-engineer)


**Stage 1** : _CLEAN_ - \[DONE\]

The repo used an Bash script to unpack the data. The passphrase is an unserialized lowercase SHA-256 hash of the keyword send over by email. The script automatically handle this.

When exploring data, it seems payment columns are incorrect (`cc_payments`, `paypal_payments`, `afterpay_payments`, `apple_payments`).\
Based on description from GFG Repo, these columns should contain the number of times credit card, PayPal, AfterPay and ApplePay was used as payment method. However, it does not seem to be the case, as there are only `0` and `1` values in these columns, denoted that a credit card was used or not, PayPal was used or not, etc...

The meaning of these columns is not the number of times a payment method was used, it is whether or not such payment method was used when purchasing the item.


<img width="1440" alt="Image" src="https://github.com/user-attachments/assets/94fda221-6e97-4539-b3c1-e4fae298e0d6" />

&nbsp;

With that idea in mind, the `main.py` script will load the unzip data using Spark DF and perform transformation on it to correct this misunderstanding. The column names are still being kept the same, but converted to Boolean (`True`, `False`).

After that, the Spark DF is written out to a staging area `gfg_technical_challenge/data/output`

&nbsp;

**Stage 2** : _INGEST_ - \[DONE\]

The `main.py` script also handle loading the data to DuckDB after complete writing to staging area.

&nbsp;

**Stage 3** : _ANALYZE_ - \[DONE\]
1. **What was the total revenue to the nearest dollar for customers who have paid by credit card?** - 5372281 (or 5372282)
<img width="1440" alt="Image" src="https://github.com/user-attachments/assets/4c6dfbab-aa5c-4b3d-852b-7d8ea9f88241" />

2. **What percentage of customers who have purchased female items have paid by credit card?** - 48.808%

3. **What was the average revenue for customers who used either iOS, Android or Desktop?** - 1484.889

4. **We want to run an email campaign promoting a new mens luxury brand. Can you provide a list of customers we should send to?** - \
This is a tricky one since in the data we do not keep track of customer's gender. As such, we can only work off the assumption that customer who purchased male items are male customers. This is not entirely true, of course, since female can also purchase male clothing, and vice versa. We can observe the distribution of male items purchased, and choose the cut-off that suitable for our campaign.

&nbsp;

**Stage 4** : _PRODUCTIONISATION_

To start off, we can use introduce crontab to automate our codes. However, in the long run, we need to also include extra tools because crontab is not flexible enough. As the number of analytic queries grew, we need orchestration tools such as Airflow to help manage. Dependency between analytic notebooks/queries is unavoidable in production environment, especially when complexity grow over time. 

Having the ability to manage & orchestrate these workflow and dependency is invaluable. It also helps with onboarding and training employees and co-workers because they do not need to spend as much time shuffling through numerous notebooks/queries to understand how the pipeline works. One simple look at the visualization of the workflow would do.

There also a need for data monitoring and alert in place to handle unsual ingestion and raise warning for action when incidents happens.

&nbsp;

## Author
Kiet Chuong

- GitHub: @chuong-k (Lost access to my old account)
- LinkedIn: linkedin.com/in/kietchuong

