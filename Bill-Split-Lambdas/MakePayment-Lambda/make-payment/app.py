import json
import stripe
import boto3


def lambda_handler(event, context):
    print(event['body'])
    stripe.api_key = "sk_test_51LHViCE10R7clMGP5gBH76hUbFeM3ogOnDqMwnfJLETPByf5wTYuOYazoy6U3KCk4LZBQV8wGleqQz92HIVsB7oh00cV8A6CnG"

    db = boto3.client('dynamodb')

    table_name = 'Resturant-AccountID'

    key = {'name': {'S': event['pathParameters']['name']}}

    response = db.get_item(TableName=table_name, Key=key)

    connected_account_id = response['Item']['accountID']['S']

    print('account id is '+connected_account_id)

    foods = []

    for item in event['body']['items']:
        # TODO: search for item in database and get the price ID
        price_id = item
        foods.append({
            "price": price_id,
            "quantity": 1
        })

    checkout = stripe.checkout.Session.create(
        mode="payment",
        line_items=foods,
        payment_intent_data={"application_fee_amount": 123},
        success_url="https://example.com/success",
        cancel_url="https://example.com/cancel",
        stripe_account=connected_account_id,
    )

    return {
        "statusCode": 200,
        "body": json.dumps({
            # "url": checkout.url,
            "foods": foods,
        }),
    }
