## Stripe angular auth

Authentication to Stripe in AngularJS using satellizer.

This is modifed from satellizer examples.

Stripe social authentication is added and some bugs are fixed for facebook.

## Reference

API call for account detail info:

curl https://api.stripe.com/v1/accounts/account_id -u api_key

Sample response:

{
  "business_logo": null, 
  "business_name": null, 
  "business_url": null, 
  "charges_enabled": false, 
  "country": "CA", 
  "default_currency": "cad", 
  "details_submitted": false, 
  "display_name": "Cameron's shop", 
  "email": "jason.cameron0714@gmail.com", 
  "id": "acct_18lYV1EXmeK987fw", 
  "managed": false, 
  "metadata": {}, 
  "object": "account", 
  "statement_descriptor": null, 
  "support_email": null, 
  "support_phone": null, 
  "timezone": "America/Vancouver", 
  "transfers_enabled": false
}

Sample access_token response from python backend:

{u'stripe_publishable_key': u'pk_test_dIJMBrOjaDvwByh3T3penJ4N', u'access_token': u'sk_test_V5M093Kbl423f23fug8GzjMC', u'livemode': False, u'token_type': u'bearer', u'scope': u'read_only', u'refresh_token': u'rt_9RlyiQ5ys6rewS4idvaWp7bPS4IyMEtpoG2Qxv3mvHEHpCUH', u'stripe_user_id': u'acct_189ISyFsev2k4j5E'}

