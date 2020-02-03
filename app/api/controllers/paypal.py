from app import cache
import paypalrestsdk

import inspect
from flask import current_app
from . import sdk


#############################################################################
# Customize the Payment window with Website Content
#
#   see:https://github.com/paypal/PayPal-Python-SDK/blob/master/samples/payment_experience/web_profile/create_payment_with_customized_experience.py
#############################################################################
#
# Name needs to be unique so just generating a random one
wpn = ''.join(random.choice(string.ascii_uppercase) for i in range(12))
print(wpn)
#
# web_profile = paypalrestsdk.WebProfile({
#     "name": wpn,
#     "presentation": {
#         "brand_name": "YeowZa Paypal",
#         "logo_image": "http://s3-ec.buzzfed.com/static/2014-07/18/8/enhanced/webdr02/anigif_enhanced-buzz-21087-1405685585-12.gif",
#         "locale_code": "US"
#     },
#     "input_fields": {
#         "allow_note": True,
#         "no_shipping": 1,
#         "address_override": 1
#     },
#     "flow_config": {
#         "landing_page_type": "billing",
#         "bank_txn_pending_url": "http://www.yeowza.com"
#     }
# })
#
# if web_profile.create():
#     print("Web Profile[%s] created successfully" % (web_profile.id))
# else:
#     print(web_profile.error)


#############################################################################
# Configure the PayPal SDK
#
#   see: https://github.com/paypal/PayPal-Python-SDK/blob/master/README.md
#############################################################################
paypalrestsdk.configure({
  'mode': current_app.config['PAYPAL_MODE'],
  'client_id': current_app.config['PAYPAL_CLIENT_ID'],
  'client_secret': current_app.config['PAYPAL_CLIENT_SECRET']
  })


#############################################################################
# Create A Payment
#
#
#   Refer to https://developer.paypal.com/docs/integration/direct/explore-payment-capabilities/
#   and to https://developer.paypal.com/docs/release-notes/#updates-for-13-august-2014 to explore
#   extra payment options available such as fee, tax, shipping discount,
#   invoice number etc.
#############################################################################
#
Invoice = paypalrestsdk.Payment({
# payment = paypalrestsdk.Payment({
#     "intent": "sale",
#     "redirect_urls": {
#         "return_url": "http://www.return.com",
#         "cancel_url": "http://www.cancel.com"
#     },
#     "payer": {
#         "payment_method": "paypal",
#         "payer_info": {
#             "tax_id_type": "BR_CPF",
#             "tax_id": "Fh618775690"
#         }
#     },
#     "transactions": [
#         {
#             "amount": {
#                 "total": "34.07",
#                 "currency": "USD",
#                 "details": {
#                     "subtotal": "30.00",
#                     "tax": "0.07",
#                     "shipping": "1.00",
#                     "handling_fee": "1.00",
#                     "shipping_discount": "1.00",
#                     "insurance": "1.00"
#                 }
#             },
#             "description": "This is the payment transaction description.",
#             "custom": "PP_EMS_90048630024435",
#             "invoice_number": "48787589677",
#             "payment_options": {
#                 "allowed_payment_method": "INSTANT_FUNDING_SOURCE"
#             },
#             "soft_descriptor": "ECHI5786786",
#             "item_list": {
#                 "items": [
#                     {
#                         "name": "bowling",
#                         "description": "Bowling Team Shirt",
#                         "quantity": "5",
#                         "price": "3",
#                         "tax": "0.01",
#                         "sku": "1",
#                         "currency": "USD"
#                     },
#                     {
#                         "name": "mesh",
#                         "description": "80s Mesh Sleeveless Shirt",
#                         "quantity": "1",
#                         "price": "17",
#                         "tax": "0.02",
#                         "sku": "product34",
#                         "currency": "USD"
#                     },
#                     {
#                         "name": "discount",
#                         "quantity": "1",
#                         "price": "-2.00",
#                         "sku": "product",
#                         "currency": "USD"
#                     }
#                 ],
#                 "shipping_address": {
#                     "recipient_name": "Betsy Buyer",
#                     "line1": "111 First Street",
#                     "city": "Saratoga",
#                     "country_code": "US",
#                     "postal_code": "95070",
#                     "state": "CA"
#                 }
#             }
#         }
#     ]
})

#
# # Create Payment and return status

# if payment.create():
#     print("Payment[%s] created successfully" % (payment.id))
#     # Redirect the user to given approval url
#     for link in payment.links:
#         if link.rel == "approval_url":
#             # Convert to str to avoid google appengine unicode issue
#             # https://github.com/paypal/rest-api-sdk-python/pull/58
#             approval_url = str(link.href)
#             print("Redirect for approval: %s" % (approval_url))
# else:
#     print("Error while creating payment:")
#     print(payment.error)
#


#############################################################################
#                              Execute Payment
#
#   see: https://github.com/paypal/PayPal-Python-SDK/blob/master/README.md
#############################################################################
#
# payment = paypalrestsdk.Payment.find("PAY-57363176S1057143SKE2HO3A")
#
# if payment.execute({"payer_id": "DUFRQ8GWYMJXC"}):
#   print("Payment execute successfully")
# else:
#   print(payment.error) # Error Hash
#


#############################################################################
#                              Get Payment details
#
#   see: https://github.com/paypal/PayPal-Python-SDK/blob/master/README.md
#############################################################################
#
# # Fetch Payment
# payment = paypalrestsdk.Payment.find("PAY-57363176S1057143SKE2HO3A")
#
# # Get List of Payments
# payment_history = paypalrestsdk.Payment.all({"count": 10})
# payment_history.payments
#
