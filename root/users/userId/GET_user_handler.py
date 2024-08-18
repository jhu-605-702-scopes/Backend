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


def get_user_handler(event, context):
    '''Demonstrates a simple HTTP endpoint using API Gateway. You have full
    access to the request and response payload, including headers and
    status code.

    To scan a DynamoDB table, make a GET request with the TableName as a
    query string parameter. To put, update, or delete an item, make a POST,
    PUT, or DELETE request respectively, passing in the payload to the
    DynamoDB API as a JSON body.
    '''
    # print("Received event: " + json.dumps(event, indent=2))

    operation = event['context']['http-method']

    if operation == "GET":
        userId = event["params"]["path"]["userId"]
        # emojis = generateCoolEmojis()
        table = dynamo.Table(table_name)
        item = table.get_item(Key={
            'userId': userId})['Item']
        print("item: ", item)
        user = {"id": item['userId'],
                     "name": item['name'] if ('name' in item) else None,
                     "username": item['username'] if ('username' in item) else None,
                     "email": item['email'] if ('email' in item) else None}

        return respond(None, user)
    else:
        return respond(ValueError('Unsupported method "{}"'.format(operation)))
