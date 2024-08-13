import boto3
import json

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


def post_user_handler(event, context):
    '''Demonstrates a simple HTTP endpoint using API Gateway. You have full
    access to the request and response payload, including headers and
    status code.

    To scan a DynamoDB table, make a GET request with the TableName as a
    query string parameter. To put, update, or delete an item, make a POST,
    PUT, or DELETE request respectively, passing in the payload to the
    DynamoDB API as a JSON body.
    '''
    #print("Received event: " + json.dumps(event, indent=2))


    operation = event['context']['http-method']

    if operation == "POST":
        # TODO any sort of data validation
        body = json.load(event["body"])
        if "userId" not in body.keys():
            body["userId"] = generate_uuid()
        table = dynamo.Table(table_name)
        resp = table.put_item(Item = body)
        return respond(None, resp)
    else:
        return respond(ValueError('Unsupported method "{}"'.format(operation)))

