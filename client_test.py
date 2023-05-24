import boto3, json
lambda_client = boto3.client('lambda')

test_event={
	"user_name":"ariel",
	"password":"seret"
}


response = lambda_client.invoke(
  FunctionName='abenillouche',
  Payload=json.dumps(test_event),
)
print(response['Payload'])
print(response['Payload'].read().decode("utf-8"))