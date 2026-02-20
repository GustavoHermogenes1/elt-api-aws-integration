import boto3

def upload_s3(file_path:str, bucket_s3:str, filename:str) -> None:
    try:
        s3 = boto3.client('s3')
        s3.upload_file(file_path, bucket_s3, filename)

    except Exception as e:
        print(f'Erro ao enviar arquivo para o S3: {e}')