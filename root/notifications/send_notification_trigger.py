import json
import boto3

sns_client = boto3.client('sns')

# Scopes-iOS ARN for SNS
APPLICATION_ARN = 'arn:aws:sns:us-east-1:010928195855:app/APNS_SANDBOX/Scopes-iOS'

def respond(err, res=None):
    return {
        'statusCode': '400' if err else '200',
        'body': json.dumps({"error": str(err)}) if err else json.dumps(res),
        'headers': {
            'Content-Type': 'application/json',
        },
    }

def send_notification(event, context):
    try:
        # Get all user tokens
        response = sns_client.list_endpoints_by_platform_application(
            PlatformApplicationArn=APPLICATION_ARN
        )
        endpoints = [
            endpoint['EndpointArn'] for endpoint in response['Endpoints'] if endpoint['Attributes']['Enabled'] == 'true'
        ]
        # Send notification to all users
        for endpoint in endpoints:
            sns_client.publish(
                TargetArn=endpoint,
                Message="Your Emoji-Scope is ready!",
                MessageStructure='string'
            )
        return(respond(None, "Successfully sent notifications"))
    except Exception as e:
        return respond(e)