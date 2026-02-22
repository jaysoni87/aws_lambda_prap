import boto3
import uuid

dynamodb = boto3.resource('dynamodb')
table_name = "TestTable"

def lambda_handler(event, context):
    table = dynamodb.Table(table_name)

    item = {
        "id": str(uuid.uuid4()),
        "name": event.get("name"),
        "age": event.get("age")
    }

    table.put_item(Item=item)

    return {
        "statusCode": 200,
        "message": "Item inserted successfully",
        "item": item
    }