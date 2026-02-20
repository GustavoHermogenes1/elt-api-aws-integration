import boto3
import io
import json

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