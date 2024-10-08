
import boto3
import json
from boto3.dynamodb.conditions import Key

print('Loading function')

dynamo = boto3.resource('dynamodb', region_name="us-east-1")
table_name = 'Users'


def respond(err, res=None):
    return {
        'statusCode': '400' if err else '200',
        'body': json.dumps({"error": str(err)}) if err else json.dumps(res),
        'headers': {
            'Content-Type': 'application/json',
        },
    }


def delete_user_handler(event, context):
    '''Demonstrates a simple HTTP endpoint using API Gateway. You have full
    access to the request and response payload, including headers and
    status code.

    To scan a DynamoDB table, make a GET request with the TableName as a
    query string parameter. To put, update, or delete an item, make a POST,
    PUT, or DELETE request respectively, passing in the payload to the
    DynamoDB API as a JSON body.
    '''
    print("Received event: " + json.dumps(event, indent=2))

    operation = event['context']['http-method']

    if operation == "DELETE":
        userId = event["params"]["path"]["userId"]
        print(event["params"]["path"])
        table = dynamo.Table(table_name)
        item = table.delete_item(Key={
            'userId': userId})

        return respond(None, item)
    else:
        return respond(ValueError('Unsupported method "{}"'.format(operation)))


