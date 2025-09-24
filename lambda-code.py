import json
import boto3
import urllib.parse

s3 = boto3.client('s3')

def lambda_handler(event, context):
    # Extrai bucket e key do evento S3
    bucket = event['Records'][0]['s3']['bucket']['name']
    key = urllib.parse.unquote_plus(event['Records'][0]['s3']['object']['key'], encoding='utf-8')
    
    # Lista objetos no bucket (exemplo de automação)
    response = s3.list_objects_v2(Bucket=bucket)
    
    # Loga no CloudWatch
    print(f"Arquivo '{key}' uploadado no bucket '{bucket}'. Objetos totais: {len(response.get('Contents', []))}")
    
    return {
        'statusCode': 200,
        'body': json.dumps(f'Processado: {key} no {bucket}')
    }
