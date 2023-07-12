import json
import boto3

# import requests


def lambda_handler(event, context):
    print(event['body'])
    body = json.loads(event['body'])
    client = boto3.client('cognito-idp')
    user_pool_id = "us-east-1_f3wPwgOY0"

    response = client.create_group(
        UserPoolId=user_pool_id,
        GroupName=body['restaurant_name'] + '_group',
        Description='group for ' + body['restaurant_name'],
    )

    create_user_response = client.admin_create_user(
        UserPoolId=user_pool_id,
        Username=body['username'],
        UserAttributes=[
            {
                'Name': 'name',
                'Value': body['name']
            },
            {
                'Name': 'custom:restaurant_name',
                'Value': body['restaurant_name']
            }
            ,
            {
                'Name': 'email',
                'Value': body['email']
            }
            ,
            {
                'Name': 'phone_number',
                'Value': body['phone']
            }
        ],
        MessageAction='SUPPRESS',
    )

    set_user_password_response = client.admin_set_user_password(
        UserPoolId=user_pool_id,
        Username=body['username'],
        Password=body['password'],
        Permanent=True
    )

    client.admin_add_user_to_group(
        UserPoolId=user_pool_id,
        Username=body['username'],
        GroupName=body['restaurant_name'] + '_group'
    )

    return {
        "statusCode": 200,
        "body": json.dumps({
            "message": "Group and user created successfully for" + body['restaurant_name'],
            # "location": ip.text.replace("\n", "")
        }),
    }
