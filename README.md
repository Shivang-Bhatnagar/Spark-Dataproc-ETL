# Spark Dataproc ETL Pipeline

This project demonstrates an end-to-end ETL (Extract, Transform, Load) data pipeline using **Apache Spark** on **Google Cloud Dataproc**. The pipeline reads the transaction data in CSV file format from HDFS, performs data Cleaning, Filtering, Transformations, and writes the results to a Hive table or HDFS in Parquet Format.

---

## Table of Contents

- [Overview](#overview)
- [Architecture](#architecture)
- [Features](#features)
- [Project Structure](#project-structure)
- [Prerequisites](#prerequisites)
- [Setup](#setup)
- [Usage](#usage)
- [Customization](#customization)
- [Troubleshooting](#troubleshooting)
- [License](#license)
- [Acknowledgements](#acknowledgements)

---

## Overview

This project is designed to:
- Ingest raw CSV data from Google Cloud Storage (GCS) or HDFS.
- Clean and transform the data using PySpark.
- Write the processed data to a Hive table or HDFS, optionally partitioned by a column (e.g., `Year`).

---

## Architecture
[CSV Data in GCS/HDFS]

|
v
[Spark ETL Job]

|
v
[Transformed Data in Hive/HDFS]


---

## Features

- Read data from CSV files
- Data cleaning and transformation using PySpark
- Partitioned writes to Hive or HDFS
- Optimized for scalable execution on Dataproc clusters
- Easily customizable for different data schemas

---

## Project Structure

├── main.py # Main Spark ETL script
├── requirements.txt # Python dependencies (if any)
├── README.md # Project documentation
└── data/ # (Optional) Sample input data


---

## Prerequisites

- **Google Cloud Platform** account
- **Google Cloud SDK** installed ([instructions](https://cloud.google.com/sdk/docs/install))
- **Dataproc cluster** (recommended: >=2 vCPUs, >=8GB RAM per node)
- **Python 3.x**
- **Apache Spark** (if running locally)

---

## Setup

### 1. Clone the Repository

git clone https://github.com/Shivang-Bhatnagar/Spark-Dataproc-ETL.git
cd Spark-Dataproc-ETL


### 2. (Optional) Install Python Dependencies

If you have a `requirements.txt` file:
Or you can simply import all the necessary libraries in the Spark Application


### 3. Configure Input and Output Paths

Edit `main.py` to set your input CSV path and output Hive/HDFS path as needed.

---

## Usage

### **A. Running on Google Cloud Dataproc**

1. **Upload your script to a GCS bucket** (optional, but recommended):

    ```
    gsutil cp main.py gs://<your-bucket>/
    ```

2. **Submit the Spark job:**

    ```
    gcloud dataproc jobs submit pyspark gs://<your-bucket>/main.py \
      --cluster=<your-cluster-name> \
      --region=<your-region>
    ```

   - Replace `<your-bucket>`, `<your-cluster-name>`, and `<your-region>` with your actual values.

### **B. Running Locally (for small data/testing)**

> **Note:** You must have Spark and Java installed locally.


---

## Customization

- **Transformation Logic:**  
  Edit `main.py` to change how data is cleaned, transformed, or partitioned.
- **Input/Output Paths:**  
  Modify the file paths in `main.py` to point to your actual data sources and destinations.
- **Spark Configurations:**  
  Adjust resource settings in your `spark-submit` command or within `main.py` (e.g., shuffle partitions, memory).

---

## Troubleshooting

- **Job is slow or stuck:**  
  - Check cluster resources; scale up if needed.
  - Lower `spark.sql.shuffle.partitions` for small clusters.
- **Job fails with Py4J or Java errors:**  
  - Ensure you are running on a proper Spark environment (Dataproc or local with Spark/Java installed).
- **Permission errors:**  
  - Check IAM permissions for GCS, HDFS, or Hive.
- **Schema mismatch:**  
  - Ensure DataFrame schema matches the Hive table schema.

---

## Acknowledgements

- [Apache Spark](https://spark.apache.org/)
- [Google Cloud Dataproc](https://cloud.google.com/dataproc)
- [PySpark Documentation](https://spark.apache.org/docs/latest/api/python/)

---



