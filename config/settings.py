from pathlib import Path

# Paths base
BASE_DIR = Path(__file__).resolve().parents[1]

DATA_DIR = BASE_DIR / "data"

BRONZE_DIR = DATA_DIR / "bronze"
SILVER_DIR = DATA_DIR / "silver"
GOLD_DIR = DATA_DIR / "gold"

# API
API_BASE = 'https://v1.formula-1.api-sports.io'
STATUS_API_URL = "https://v1.formula-1.api-sports.io/status"
TIMES_API_URL = "https://v1.formula-1.api-sports.io/teams"
RACES_API_URL = "https://v1.formula-1.api-sports.io/races"
RANKING_API_URL = "https://v1.formula-1.api-sports.io/rankings/teams"
CIRCUIT_API_URL = "https://v1.formula-1.api-sports.io/circuits"
API_TIMEOUT = 30

# AWS
AWS_REGION = "us-east-2"
S3_BUCKET = "api-aws-integration-pipeline-project"

# S3 Prefix
S3_BRONZE_PREFIX = "bronze"
S3_SILVER_PREFIX = "silver"

# DOTENV
DOTENV_DIR = BASE_DIR / '.env'