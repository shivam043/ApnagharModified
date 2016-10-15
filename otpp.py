# Download the twilio-python library from http://twilio.com/docs/libraries
from twilio.rest import TwilioRestClient
from random import randint
#c=randint(99999,1000000)
# Find these values at https://twilio.com/user/account
account_sid = "ACca0c205d4af1c525be1c1166bcfcd1c2"
auth_token = "b0f4e93e76462769010f0d70920ab93a"
client = TwilioRestClient(account_sid, auth_token)
message = client.messages.create(to="+919811420140", from_="+15034063163",
                                     body="Dear user ,your order for Audio Technica Ath-Cor150bl Blue In-The-Ear Hp's earphones has been cancelled . Corresponding amount will be transferred in your account within 7 working days.Thank you for shopping with us.Team Amazon.")


