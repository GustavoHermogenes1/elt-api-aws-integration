import boto3
import io
import json
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