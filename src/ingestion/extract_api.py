import requests
import json
from config.settings import BRONZE_DIR

def extract_data_api(api_name:str, api_url:str, headers:dict, params:dict | None = None) -> list[dict]:
    try:
        response = requests.get(api_url, headers=headers, params=params)
        data = response.json()

        file_path = f'{BRONZE_DIR}/{api_name}_raw.json'

        with open(file_path, 'w', encoding='utf-8') as f:
            json.dump(data, f, ensure_ascii=False, indent=4)
            print(f'Arquivo raw salvo em:\n{file_path}')

        return data
    except Exception as e:
        print(f'Não foi possível realizar a requisição e salvar o arquivo raw. Erro:\n{e}')