# Documentation 

This API lets the Restaurant owner to upload his menu to Stripe as a csv file or JSON

The end point for this POST request is https://lwppeajj4d.execute-api.us-east-1.amazonaws.com/Prod/upload/{restaurantName}

## Parameters
You must include the restaurant name in the path of the request

## Headers
You must include the Content-Type header with the value application/json if you're uplaoding a JSON file or text/csv if you're uploading a CSV file

## Body
You must include the body of the request with the file you want to upload

## Response
The response will be a JSON object with the following structure:

```json
{
    "message": "File uploaded successfully"
}
```
