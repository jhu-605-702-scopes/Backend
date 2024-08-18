import boto3
import json
import emoji_generator.random_emoji as emojigen
from boto3.dynamodb.conditions import Key
from botocore.exceptions import ClientError

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


def post_horoscope_handler(event, context):
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
        userId = event["params"]["path"]["userId"]
        date = event["params"]["path"]["date"]
        body = event["body-json"]
        feedback = ""
        emojis = generateCoolEmojis()
        if body:
            print(body)
            feedback = body.get("feedback", "")
            emojis: body.get("emojis", emojis)
        horoscope = {"userId": userId, "date": str(date), "emojis": str(emojis), "feedback": feedback}
        table = dynamo.Table(table_name)
        try:
            resp = table.put_item(Item = horoscope)
            return respond(None, horoscope)
        except ClientError as e:
            return respond(ClientError, None)
    else:
        return respond(ValueError('Unsupported method "{}"'.format(operation)))

def generateCoolEmojis():
    # [{'code': 'U+3299', 'name': 'Japanese “secret” button', 'image': '㊙', 'category': 'Symbols'}, {'code': 'U+1F6F8', 'name': 'flying saucer', 'image': '🛸', 'category': 'Travel & Places'}, {'code': 'U+271D', 'name': 'latin cross', 'image': '✝', 'category': 'Symbols'}]
    return [(emojigen.get_random_emojis(1)[0]["image"]) for x in range(3)]
