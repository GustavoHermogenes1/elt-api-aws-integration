import pandas as pd
import pyarrow as pa
import pyarrow.parquet as pq
<<<<<<< HEAD
import os


def transform_json_to_parquet(data: dict, file_name: str, dir_path: str):

    try:

        if not isinstance(data, dict):
            raise ValueError("Formato de dados inválido. Esperado dict.")

        if "response" not in data:
            raise ValueError("Campo 'response' não encontrado no JSON da API.")

        response = data["response"]

        if not response:
            raise ValueError("API retornou response vazio.")

        # normaliza JSON
        df = pd.json_normalize(response)

        # garante diretório
        os.makedirs(dir_path, exist_ok=True)

        output_path = os.path.join(dir_path, file_name)

        # converte para Arrow
        table = pa.Table.from_pandas(df)

        # salva parquet
        pq.write_table(table, output_path)

        print(f"Parquet salvo: {output_path}")

        return output_path

    except Exception as e:
        raise Exception(f"Erro na transformação JSON -> Parquet: {e}")
=======
import io
import os

def transform_json_to_parquet(data:list[dict], file_name:str, dir_path:str) -> io.BytesIO:
    try:
        df = pd.json_normalize(data)

        table = pa.Table.from_pandas(df)
        
        buffer = io.BytesIO()
        pq.write_table(table, buffer)

        buffer.seek(0)

        if dir_path:
            output_path = os.path.join(dir_path, file_name)
            pq.write_table(table, output_path)
            print(f'Arquivo Parquet salvo em:\n{output_path}')
        
        return buffer
    
    except Exception as e:
        print(f'Erro ao converter os dados .json para parquet:\n{e}')
>>>>>>> 7b1d72ea7b5f713b66d843d3764b88cf2dbb4da2
