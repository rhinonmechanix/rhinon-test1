import boto3
dynamodb = boto3.resource('dynamodb')
table = dynamodb.Table('users')

response = table.scan()
item = response["Items"]
for x in item:
    print(x)