import json
import stripe

# import requests


def lambda_handler(event, context):
    """Sample pure Lambda function

    Parameters
    ----------
    event: dict, required
        API Gateway Lambda Proxy Input Format

        Event doc: https://docs.aws.amazon.com/apigateway/latest/developerguide/set-up-lambda-proxy-integrations.html#api-gateway-simple-proxy-for-lambda-input-format

    context: object, required
        Lambda Context runtime methods and attributes

        Context doc: https://docs.aws.amazon.com/lambda/latest/dg/python-context-object.html

    Returns
    ------
    API Gateway Lambda Proxy Output Format: dict

        Return doc: https://docs.aws.amazon.com/apigateway/latest/developerguide/set-up-lambda-proxy-integrations.html
    """

    # try:
    #     ip = requests.get("http://checkip.amazonaws.com/")
    # except requests.RequestException as e:
    #     # Send some context about this error to Lambda Logs
    #     print(e)

    #     raise e

    stripe.api_key = "sk_test_51LHViCE10R7clMGP5gBH76hUbFeM3ogOnDqMwnfJLETPByf5wTYuOYazoy6U3KCk4LZBQV8wGleqQz92HIVsB7oh00cV8A6CnG"

    account = stripe.Account.create(type="standard")

    account_link = stripe.AccountLink.create(
        account=account.id,
        refresh_url="https://example.com/reauth",
        return_url="https://example.com/return",
        type="account_onboarding",
    )

    return {
        "statusCode": 200,
        "body": json.dumps({
            "account_link": account_link.url
        }),
    }
