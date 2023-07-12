# Documentation 

This API will return a link to the Stripe onboarding page for a restaurant to set up their account for receiving payments.

The endpoint for this POST request is: https://r4wxyltq6g.execute-api.us-east-1.amazonaws.com/Prod/create

in the body of the request, you will need to include the following:

```json
{
    "name": "Restaurant Name"
}
```

The response will be formatted as follows:

```json
{
    "account_link": "https://a.link.to.the.stripe.onboarding.page"
}
```

