#source from https://www.youtube.com/watch?v=Y18HF5ALXew&t=1037s
import boto3
import json

dynamodb = boto3.resource('dynamodb')
s3 = boto3.resource('s3')
s3_client = boto3.client('s3')

def lambda_handler(event, context):
	
	bucket = event['Records'][0]['s3']['bucket']['name']
	json_file_name = event['Records'][0]['s3']['object']['key']
	json_object = s3_client.get_object(Bucket=bucket,Key=json_file_name)
	jsonFileReader = json_object['Body'].read()
	jsonDict = json.loads(jsonFileReader)
	print(str(jsonDict))
	table = dynamodb.Table('employee')
	table.put_item(Item=jsonDict)
	return {
		'statusCode': 200,
		'body': 'wow'	
	}