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


def get_horoscope_handler(event, context):
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
        date = event["params"]["path"]["date"]
        # emojis = generateCoolEmojis()
        table = dynamo.Table(table_name)
        item = table.get_item(Key={
            'userId': userId,
            'date': date})['Item']
        print("item", item)
        horoscope = {"userId": item['userId'],
                     "date": item['date'],
                     "emojis": item['emojis'],
                     "feedback": item["feedback"]}

        return respond(None, horoscope)
    else:
        return respond(ValueError('Unsupported method "{}"'.format(operation)))
