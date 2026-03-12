from airflow.decorators import dag, task
from ingestion.extract_api import extract_data_api
from processing.json_to_parquet import transform_json_to_parquet
from storage.upload_s3 import upload_data_to_s3
from config.settings import S3_BRONZE_PREFIX, S3_BUCKET, S3_SILVER_PREFIX, STATUS_API_URL, RACES_API_URL, TIMES_API_URL, CIRCUIT_API_URL, RANKING_API_URL, SILVER_DIR
from dotenv import load_dotenv
from datetime import datetime
import sys
import os

load_dotenv()

headers = {
    'x-apisports-key' : os.getenv("API_TOKEN")
}

params = {
    'season' : 2024
}

# Adiciona src ao path do container
sys.path.append("/opt/airflow/src")

@dag(
    "elt_api_pipeline",
    start_date=datetime(2026, 3, 2),
    schedule_interval=None,
    catchup=False,
    tags=['elt', 'aws']
)
def elt_pipeline():
    endpoints = {
        "status": STATUS_API_URL,
        "teams": TIMES_API_URL,
        "races": RACES_API_URL,
        "ranking": RANKING_API_URL,
        "circuits": CIRCUIT_API_URL,
    }

    @task
    def extract(endpoint_name, url):
        if endpoint_name in ["races", "ranking"]:
            return extract_data_api(endpoint_name, url, headers, params)
        return extract_data_api(endpoint_name, url, headers)
    
    @task
    def upload_bronze(endpoint_name, data):
        upload_data_to_s3(
            data,
            S3_BUCKET,
            f"{S3_BRONZE_PREFIX}/{endpoint_name}/{endpoint_name}.json",
        )
        return data
    
    @task
    def transform(endpoint_name, data):
        return transform_json_to_parquet(
            data,
            f"{endpoint_name}.parquet",
            SILVER_DIR,
        )
    
    @task
    def upload_silver(endpoint_name, parquet_file):
        upload_data_to_s3(
            parquet_file,
            S3_BUCKET,
            f"{S3_SILVER_PREFIX}/{endpoint_name}/{endpoint_name}.parquet",
        )
    
    for name, url in endpoints.items():
        extracted = extract(name, url)
        bronze_uploaded = upload_bronze(name, extracted)
        transformed = transform(name, bronze_uploaded)
        upload_silver(name, transformed)

dag = elt_pipeline()