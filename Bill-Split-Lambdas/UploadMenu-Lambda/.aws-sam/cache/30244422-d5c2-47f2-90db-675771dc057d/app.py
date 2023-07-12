import base64
import json
import stripe
import re
import boto3
import csv


def lambda_handler(event, context):
    stripe.api_key = "sk_test_51LHViCE10R7clMGP5gBH76hUbFeM3ogOnDqMwnfJLETPByf5wTYuOYazoy6U3KCk4LZBQV8wGleqQz92HIVsB7oh00cV8A6CnG"
    print(event)
    print('the path param is ' + event['pathParameters']['name'])

    db = boto3.client('dynamodb')

    table_name = 'Resturant-AccountID'

    key = {'name': {'S': event['pathParameters']['name']}}

    response = db.get_item(TableName=table_name, Key=key)

    account_id = response['Item']['accountID']['S']
    print('Account ID is ' + account_id)

    content_type = event['headers']['Content-Type']
    print('The Content Type is ' + event['headers']['Content-Type'])

    if content_type == 'application/json':

        # Extract JSON string from event
        match = re.search(r"{.*}", event['body'], re.DOTALL)
        json_string = match.group()

        # Parse JSON string into a dictionary
        menu_dict = json.loads(json_string)

        # Extract food name and price from menu items and create dictionary
        food_dict = {item["Name"]: item["Price"] for item in menu_dict["menu"]}

        # Create Stripe products and prices for each menu item
        for food in food_dict:
            product = stripe.Product.create(
                name=food,
                stripe_account=account_id
            )

            stripe.Price.create(
                unit_amount=int(round(float(food_dict[food]) * 100)),
                currency='usd',
                product=product.id,
                stripe_account=account_id
            )

        print(food_dict)

        return {
            "statusCode": 200,
            "body": json.dumps({
                "message": "File uploaded successfully",
            }),
        }

    elif content_type == 'text/csv' or content_type == 'multipart/form-data':
        file_content = base64.b64decode(event['body'])
        output = file_content.decode('utf-8-sig').splitlines()

        print(output)
        print('output at index 5 ' + output[5])

        food_dict = {}
        for row in csv.reader(output[5:]):
            try:
                product = stripe.Product.create(
                    name=row[0],
                    stripe_account=account_id
                )

                stripe.Price.create(
                    unit_amount=int(round(float(row[1]) * 100)),
                    currency='usd',
                    product=product.id,
                    stripe_account=account_id
                )
                food_dict[row[0]] = float(row[1])
                print(row[0], row[1])
            except IndexError:
                print(food_dict)
                return {
                    "statusCode": 200,
                    "body": json.dumps({
                        "message": "File uploaded successfully",
                    }),
                }

        print(food_dict)
