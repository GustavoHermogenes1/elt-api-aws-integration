import pandas as pd
import pyarrow as pa
import pyarrow.parquet as pq
import io

def transform_json_to_parquet(data:list[dict], output_path:str) -> io.BytesIO:
    try:
        df = pd.json_normalize(data)

        table = pa.Table.from_pandas(df)
        
        buffer = io.BytesIO()
        pq.write_table(table, buffer)

        buffer.seek(0)

        print(f'Arquivo Parquet salvo em:\n{output_path}')
        
        return buffer
    
    except Exception as e:
        print(f'Erro ao converter os dados .json para parquet:\n{e}')