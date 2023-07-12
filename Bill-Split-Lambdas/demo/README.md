# Documentation

This API in theory will let you create or get a table order from the MongoDB.

The endpoint for the POST request is https://2mmt3rbyj0.execute-api.us-east-1.amazonaws.com/Prod/table

In the body of the request you must include the following:

id - the table id as an Integer

items - a list of MenuItems
```json
{
    "id": 1,
    "items": [
        {
            "name": "Steak",
            "price": 4.00
        },
        {
            "name": "Pasta",
            "price": 4.00
        },
        {
            "name": "Pizza",
            "price": 4.00
        }
    ]
}
```

The endpoint for the GET request is https://2mmt3rbyj0.execute-api.us-east-1.amazonaws.com/Prod/table/{id}

The response will be formatted as follows:

```json
[
    {
        "name": "Steak",
        "price": 4.0
    },
    {
        "name": "Pasta",
        "price": 4.0
    },
    {
        "name": "Pizza",
        "price": 4.0
    }
]
```

