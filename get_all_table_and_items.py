import boto3
dynamodb = boto3.resource('dynamodb')

for table in dynamodb.tables.all():
        tableName = table.name
        print(tableName)
        table = dynamodb.Table(tableName)
        response = table.scan()
        item = response["Items"]
        f = open("demofile.json", "a")
        f.write(tableName)
        f.write("\n")
        f.close()
        for x in item:
            print(x)
            f = open("demofile.json", "a")
            f.write(str(x))
            f.write("\n")
            f.close()
        