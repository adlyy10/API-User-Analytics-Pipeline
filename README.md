# API User Analytics Pipeline

## Project Overview

This project is a small ETL pipeline built with Python and pandas.

The pipeline:

* extracts raw user data from JSON API data
* transforms nested JSON fields
* generates analytics KPIs
* exports clean CSV reports

## Technologies Used

* Python
* pandas

## Features

* JSON ingestion
* Nested JSON extraction
* Data transformation
* KPI generation
* CSV exports
* Modular ETL structure

## Generated Reports

* clean_users.csv
* users_per_city.csv
* users_per_company.csv

## Project Structure

api-user-analytics-pipeline/
│
├── output/
├── users.json
├── pipeline.py
├── requirements.txt
└── README.md

## How to Run

```bash
pip install -r requirements.txt
python pipeline.py
```
