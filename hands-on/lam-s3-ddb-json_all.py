import json
import boto3

s3_client = boto3.client('s3')
dynamodb = boto3.resource('dynamodb')

def lambda_handler(event, context):
	list = []
	for record in event['Records']:
		bucket = record['s3']['bucket']['name']
		json_file_name = ['s3']['object']['key']
		json_object = s3_client.get_object(Bucket=bucket,Key=json_file_name)
		jsonFileReader = json_object['Body'].read()
		jsonDict = json.loads(jsonFileReader)
		print(str(jsonDict))
		#table = dynamodb.Table('personal_info')
		table = dynamodb.Table('employee2')
		for people in jsonDict['person']:
			table.put_item(Item=people)
		return 'put dynamodb table S3 bucket json data through  Lambda'