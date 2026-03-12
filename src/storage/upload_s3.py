import boto3
import io
import json
<<<<<<< HEAD
from pathlib import Path

def upload_data_to_s3(data, bucket_s3: str, file_path: str):

    s3 = boto3.client("s3")

    if isinstance(data, (dict, list)):
        buffer = io.BytesIO(json.dumps(data).encode("utf-8"))

    elif isinstance(data, (str, Path)):
        with open(data, "rb") as f:
            buffer = io.BytesIO(f.read())

    elif isinstance(data, io.BytesIO):
        buffer = data

    else:
        raise ValueError("Formato de dados não suportado")

    buffer.seek(0)

    s3.upload_fileobj(buffer, bucket_s3, file_path)

    print(f"Upload realizado: s3://{bucket_s3}/{file_path}")
=======

def upload_data_to_s3(data: dict | list | io.BytesIO, bucket_s3:str, file_path:str) -> None:
    try:
        s3 = boto3.client('s3')

        if isinstance(data, io.BytesIO):
            buffer = data
        else:
            buffer = io.BytesIO(json.dumps(data).encode("utf-8"))

        s3.upload_fileobj(buffer, bucket_s3, file_path)
        print(f'Upload de arquivo feito no bucket:\n{bucket_s3}')

    except Exception as e:
        print(f'Erro ao enviar arquivo para o S3: {e}')
>>>>>>> 7b1d72ea7b5f713b66d843d3764b88cf2dbb4da2
