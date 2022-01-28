import boto3
dynamodb = boto3.resource('dynamodb')
table = dynamodb.Table('users')

table.put_item(
   Item={
        'username': 'dev',
        'first_name': 'john',
        'last_name': 'Doe',
        'age': 25,
        'account_type': 'standard_user',
    }
)