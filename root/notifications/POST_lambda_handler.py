import boto3
import json

print('Loading notifications function')

sns = boto3.client('sns', region_name="us-east-2")
topic_arn = 'arn:aws:sns:us-east-1:819873747797:scopes'

def respond(err, res=None):
    return {
        'statusCode': '400' if err else '200',
        'body': json.dumps({"error": str(err)}) if err else json.dumps(res),
        'headers': {
            'Content-Type': 'application/json',
        },
    }


def lambda_handler(event, context):
    '''Registers a user's notification token with the SNS service'''
    operation = event['httpMethod']
    if operation == "POST":
        body = json.load(event["body"])
        if "token" not in body.keys():
            return respond(ValueError('Missing token in body'))
        try:
            sns.subscribe(
                TopicArn=topic_arn,
                Protocol='application',
                Endpoint=body["token"]
            )
            return respond(None, "Success")
        except Exception as e:
            return respond(e)

    else:
        return respond(ValueError('Unsupported method "{}"'.format(operation)))