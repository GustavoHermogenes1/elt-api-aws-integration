from src.ingestion.extract_api import extract_data_api
from src.processing.json_to_parquet import transform_json_to_parquet
from src.storage.upload_s3 import upload_data_to_s3
from dotenv import load_dotenv
import os
from config.settings import STATUS_API_URL, TIMES_API_URL, RACES_API_URL, RANKING_API_URL, CIRCUIT_API_URL, S3_BUCKET, SILVER_DIR, S3_BRONZE_PREFIX, S3_SILVER_PREFIX

load_dotenv()

headers = {
    'x-apisports-key' : os.getenv("API_TOKEN")
}

params = {
    'season' : 2024
}

# API Data Extraction
status = extract_data_api('status', STATUS_API_URL, headers)
teams = extract_data_api('teams', TIMES_API_URL, headers)
races = extract_data_api('races', RACES_API_URL, headers, params)
ranking = extract_data_api('ranking', RANKING_API_URL, headers, params)
circuits = extract_data_api('circuits', CIRCUIT_API_URL, headers)

# Converting JSON to Parquet
status_parquet = transform_json_to_parquet(status, SILVER_DIR)
teams_parquet = transform_json_to_parquet(teams, SILVER_DIR)
races_parquet = transform_json_to_parquet(races, SILVER_DIR)
rankings_parquet = transform_json_to_parquet(ranking, SILVER_DIR)
circuits_parquet = transform_json_to_parquet(circuits, SILVER_DIR)

# Upload JSON to Data Lake AWS S3
upload_data_to_s3(status, S3_BUCKET, f'{S3_BRONZE_PREFIX}/status/status.json')
upload_data_to_s3(teams, S3_BUCKET, f'{S3_BRONZE_PREFIX}/teams/teams.json')
upload_data_to_s3(races, S3_BUCKET, f'{S3_BRONZE_PREFIX}/races/races.json')
upload_data_to_s3(ranking, S3_BUCKET, f'{S3_BRONZE_PREFIX}/ranking/ranking.json')
upload_data_to_s3(circuits, S3_BUCKET, f'{S3_BRONZE_PREFIX}/circuits/circuits.json')

# Upload PARQUET to Data Lake AWS S3
upload_data_to_s3(status_parquet, S3_BUCKET, f'{S3_SILVER_PREFIX}/status/status.parquet')
upload_data_to_s3(teams_parquet, S3_BUCKET, f'{S3_SILVER_PREFIX}/teams/teams.parquet')
upload_data_to_s3(races_parquet, S3_BUCKET, f'{S3_SILVER_PREFIX}/races/races.parquet')
upload_data_to_s3(rankings_parquet, S3_BUCKET, f'{S3_SILVER_PREFIX}/ranking/ranking.parquet')
upload_data_to_s3(circuits_parquet, S3_BUCKET, f'{S3_SILVER_PREFIX}/circuits/circuits.parquet')