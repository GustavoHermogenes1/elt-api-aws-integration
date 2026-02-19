from pathlib import Path

# Paths base
BASE_DIR = Path(__file__).resolve().parents[1]

DATA_DIR = BASE_DIR / "data"

BRONZE_DIR = DATA_DIR / "bronze"
SILVER_DIR = DATA_DIR / "silver"
GOLD_DIR = DATA_DIR / "gold"

# API
API_URL = "https://api.exemplo.com/data"
API_TIMEOUT = 30

# AWS
AWS_REGION = "us-east-1"
S3_BUCKET = "meu-bucket-datalake"

# S3 Prefix
S3_BRONZE_PREFIX = "bronze/api_name"
S3_SILVER_PREFIX = "silver/api_name"
