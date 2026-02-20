import pandas as pd
import pyarrow as pa
import pyarrow.parquet as pq
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