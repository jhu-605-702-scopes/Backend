import boto3
import json

print('Loading function')

dynamo = boto3.resource('dynamodb', region_name="us-east-1")
table_name = 'Horoscopes'


def respond(err, res=None):
    return {
        'statusCode': '400' if err else '200',
        'body': json.dumps({"error": str(err)}) if err else json.dumps(res),
        'headers': {
            'Content-Type': 'application/json',
        },
    }


def get_horoscope_list_handler(event, context):
    '''Demonstrates a simple HTTP endpoint using API Gateway. You have full
    access to the request and response payload, including headers and
    status code.

    To scan a DynamoDB table, make a GET request with the TableName as a
    query string parameter. To put, update, or delete an item, make a POST,
    PUT, or DELETE request respectively, passing in the payload to the
    DynamoDB API as a JSON body.
    '''
    # print("Received event: " + json.dumps(event, indent=2))

    operation = event['httpMethod']

    if operation == "GET":
        userId = event["pathParameters"]["userId"]
        table = dynamo.Table(table_name)
        items = table.query(KeyConditionExpression=Key('userId').eq(userId))["Items"]
        return respond(None, items)
    else:
        return respond(ValueError('Unsupported method "{}"'.format(operation)))
