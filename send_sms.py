# Import Twilio.
from twilio.rest import Client
# Import required hidden numbers from other file.
from my_secret_numbers import Cell_number, AUTH_TOKEN

# Codes required by twilio.
ACCOUNT_SID = 'ACaa49420ab61ad5584d34556236d5c326'
auth_token = AUTH_TOKEN

# Make our twilio client.
client = Client(ACCOUNT_SID, auth_token)
#
sender = '+12562428054'
reciever = Cell_number

# The text going to be sent out.
text = 'To be or not to be? That is my question!'
# Use the client to send the SMS text.
client.messages.create(to=reciever, from_=sender, body=text)
