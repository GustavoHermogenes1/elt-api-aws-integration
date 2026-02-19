from src.ingestion.extract_api import extract_data_api
from dotenv import load_dotenv
import os
from config.settings import STATUS_API_URL, TIMES_API_URL, RACES_API_URL, RANKING_API_URL, CIRCUIT_API_URL

load_dotenv()

headers = {
    'x-apisports-key' : os.getenv("API_TOKEN")
}

params = {
    'season' : 2024
}

extract_data_api('status', STATUS_API_URL, headers)
extract_data_api('teams', TIMES_API_URL, headers)
extract_data_api('races', RACES_API_URL, headers, params)
extract_data_api('ranking', RANKING_API_URL, headers, params)
extract_data_api('circuits', CIRCUIT_API_URL, headers)