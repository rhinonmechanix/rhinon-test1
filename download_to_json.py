import boto3
import json
Table = input("Enter the table name = ")
dynamoclient = boto3.client('dynamodb')
dynamopaginator = dynamoclient.get_paginator('scan')
def validateTables():
    print("Inside validateTables")
    try:
        dynamoclient.describe_table(TableName=Table)
        print("The table exists")
    except dynamoclient.exceptions.ResourceNotFoundException:
        print("The table does not exists")
validateTables()

def convert_json():
    print('Start Reading the Table')
    dynamoresponse = dynamopaginator.paginate(
    TableName=Table,
    Select='ALL_ATTRIBUTES',
    ReturnConsumedCapacity='NONE',
    ConsistentRead=True
    )
    for page in dynamoresponse:
        x = page['Items']
        with open('file.json', 'a') as outfile:
                outfile.write(json.dumps(x))
                outfile.close()
        print("The json file has created...")
convert_json()