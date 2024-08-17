import boto3
import json
#import emoji_generator.random_emoji as emojigen

print('Loading function')

dynamo = boto3.resource('dynamodb', region_name="us-east-2")
table_name = 'Users'

def respond(err, res=None):
    return {
        'statusCode': '400' if err else '200',
        'body': json.dumps({"error": str(err)}) if err else json.dumps(res),
        'headers': {
            'Content-Type': 'application/json',
        },
    }


def lambda_handler(event, context):
    '''Demonstrates a simple HTTP endpoint using API Gateway. You have full
    access to the request and response payload, including headers and
    status code.

    To scan a DynamoDB table, make a GET request with the TableName as a
    query string parameter. To put, update, or delete an item, make a POST,
    PUT, or DELETE request respectively, passing in the payload to the
    DynamoDB API as a JSON body.
    '''
    #print("Received event: " + json.dumps(event, indent=2))


    operation = event['httpMethod']

    if operation == "PUT":
        userId = event["pathParameters"]["userId"]
        user = json.load(event["body"])
        table = dynamo.Table(table_name)
        resp = table.put_item(Item = user)
        return respond(None, resp)
    else:
        return respond(ValueError('Unsupported method "{}"'.format(operation)))
