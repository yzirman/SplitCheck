# Documentation

This API allows a restaurant owner to create an account for FEEd. This is different than the API that allows him to create a Stripe account. This API will create an account for him so he can sign into FEEd itself.

The endpoint for the POST request is https://vopcjx2xve.execute-api.us-east-1.amazonaws.com/Prod/create

## Body
You must supply the following information in the body of the POST request:

* `restaurant_name` - The name of the restaurant. The name can not contain any special characters including spaces.
* `username` - The username he wants to create to sign in with.
* `password` - The password he wants to create to sign in with. It must contain one special character, one number, and one uppercase letter.
* `email` - The email address of the restaurant owner.
* `phone` - The phone number of the owner. Must include a + sign followed by the country code then the number with no spaces or dashes
* `name` - Name of the owner

````json
{
    "restaurant_name": "Domino",
    "username": "shulman33",
    "name": "Sam Shulman",
    "email": "email@gmail.com",
    "phone": "+19736998748",
    "password": "#Password2233"
}
````

## Response 
If the request was successful and created a user the response will be the following:

````json
{
    "message": "Group and user created successfully forDomino"
}
````
