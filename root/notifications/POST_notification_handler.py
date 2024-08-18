import boto3
import json

print('Loading notifications function')

sns = boto3.client('sns', region_name="us-east-1")
platform_application_arn = 'arn:aws:sns:us-east-1:010928195855:app/APNS_SANDBOX/Scopes-iOS'

def respond(err, res=None):
    return {
        'statusCode': '400' if err else '200',
        'body': {"error": str(err)} if err else res,
        'headers': {
            'Content-Type': 'application/json',
        },
    }


def post_notification_handler(event, context):
    operation = event['context']['http-method']
    if operation == "POST":
        body = event["body-json"]
        if body:
            token = body.get("token", "")
        if not token:
            return respond(ValueError('Token is required'))

        # register device token with SNS
        sns.create_platform_endpoint(
            PlatformApplicationArn=platform_application_arn,
            Token=token
        )

        return respond(None, {"message": "Device token registered successfully"})