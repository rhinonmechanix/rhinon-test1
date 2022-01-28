import boto3
dynamo = boto3.resource('dynamodb')
for table in dynamo.tables.all():
        print(table.name)