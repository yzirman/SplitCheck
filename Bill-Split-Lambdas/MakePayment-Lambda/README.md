# Documentation

This API will create a url for that customers checkout page with the products they have selected.

The endpoint for the POST request is: https://3v3lrexaxj.execute-api.us-east-1.amazonaws.com/Prod/pay/{name}

## Parameters
You must include the restaurant name in the path

## Body

In the body of the request, you will need to include the following:

a list of the names of the products they ordered 

```json
{
  "items": 
    [
      "Steak",
      "Chulent",
      "Fish"
    ]
}
```

The response will be a link to the checkout page with the products they have selected.

```json
{
  "url": "https://checkout.link"
}
```
