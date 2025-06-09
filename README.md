# 💳 Cloud-Based Credit Card Fraud Detection Pipeline

This project converts a Jupyter-based machine learning model into a **modular, cloud-ready data engineering pipeline** using Python, AWS S3, and PostgreSQL. It enables automated data ingestion, transformation, and loading of credit card transaction data for downstream analysis or modeling.

---

## 🧩 Key Features

- ✅ Modular ETL structure (`extract.py`, `transform.py`, `load.py`, `main.py`)
- ☁️ Cloud-native design with **S3 → PostgreSQL** integration
- 🧼 Cleans and enriches raw data with fraud flags, Z-scores, and outlier markers
- 🧪 Easily testable, scalable, and production-friendly
- 🕹️ Fully runnable from the command line or scheduled via a workflow tool

---

## ⚙️ Tech Stack

- **AWS S3** – Stores raw CSV files
- **boto3** – Connects to S3 and fetches input data
- **Pandas** – Used for cleaning, feature engineering
- **SQLAlchemy** – Loads data into PostgreSQL
- **PostgreSQL** – Stores queryable results
- **Python** – Modularized ETL scripts
- *(Optional)* Airflow-compatible structure

---

## 🔁 Pipeline Flow

S3 Bucket (raw/creditcard.csv)]

↓

[extract.py] — Downloads raw data from S3

↓

[transform.py] — Cleans, deduplicates, creates fraud flags

↓

[load.py] — Loads enriched data into PostgreSQL


---

## 📁 Project Structure


├── extract.py # Downloads data from S3

├── transform.py # Data cleaning + feature engineering

├── load.py # Loads to PostgreSQL

├── main.py # Orchestrates ETL

├── config.py # Configs (DB URI, bucket name)

├── requirements.txt

├── .gitignore

├── legacy_notebooks/ # Archived notebooks and PDFs

└── README.md

---

## 🚀 How to Run the Pipeline

### 1. Install dependencies

pip install -r requirements.txt

### 2. Set your environment (recommended: .env file or export manually)
export AWS_ACCESS_KEY_ID=your_key

export AWS_SECRET_ACCESS_KEY=your_secret

export AWS_REGION=us-west-2

export S3_BUCKET=your-bucket-name

export DATABASE_URI=postgresql://username:password@host:port/creditcard_db


### 3. Run the pipeline
python main.py

###  What’s in the Database

After running the pipeline, your PostgreSQL DB will have:

* A table: creditcard_data

* Cleaned and labeled records

* Ready for BI tools or modeling

# 🗂️ Legacy Version
The original data science notebooks and PDFs are archived in:

/legacy_notebooks/

These contain exploratory work and notebook-based models for reference.

# 📌 Why It Matters (from a Data Engineering POV)
* 📦 Modular pipeline — clean separation of extract, transform, and load logic

* ☁️ Cloud-native — integrates with AWS and PostgreSQL, can plug into Airflow or Lambda

* 💡 Extensible — future support for logging, CI/CD, or scheduling

* 📈 BI/Analytics-ready — outputs clean, SQL-friendly tables


