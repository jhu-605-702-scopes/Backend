import boto3
import json

print('Loading function')

dynamo = boto3.resource('dynamodb', region_name="us-east-1")
table_name = 'Users'

def respond(err, res=None):
    return {
        'statusCode': '400' if err else '200',
        'body': {"error": str(err)} if err else res,
        'headers': {
            'Content-Type': 'application/json',
        },
    }

def post_login_handler(event, context):
    '''Handles user login by verifying email and password.'''
    # Extract email and password from the request body
    body = json.loads(event["body"])
    email = body.get("email")
    password = body.get("password")

    if not email or not password:
        return respond(ValueError('Email and password are required'))

    table = dynamo.Table(table_name)

    # Query the table to find the user with the given email
    response = table.scan(
        FilterExpression=boto3.dynamodb.conditions.Attr('email').eq(email)
    )

    if not response['Items']:
        return respond(ValueError('Invalid email or password'))

    user = response['Items'][0]

    # Check if the provided password matches the stored password
    if user['password'] != password:
        return respond(ValueError('Invalid email or password'))

    # Return the entire user object
    return respond(None, user)