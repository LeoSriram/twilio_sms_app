# Import Twilio.
from twilio.rest import Client
# Import required hidden numbers from other file.
from my_secret_numbers import Cell_number, AUTH_TOKEN
# Import the flask framework
from flask import Flask
# This is required to respont to texts that come in.
from twilio.twiml.messaging_response import MessagingResponse

# Codes required by twilio.
ACCOUNT_SID = 'ACaa49420ab61ad5584d34556236d5c326'
auth_token = AUTH_TOKEN

# Make our twilio client.
client = Client(ACCOUNT_SID, auth_token)
# Numbers of sender and reciever
sender = '+12562428054'
reciever = Cell_number

# The text going to be sent out.
text = 'To be or not to be? That is my question!'
# Use the client to send the SMS text.
client.messages.create(to=reciever, from_=sender, body=text)

# Create our flask app
web_app = Flask(__name__)

def sms_reply():
    # Create a response object.
    automatic_response = MessagingResponse()
    # Put a message in our response object.
    automatic_response.message('This is an auto reply from Twilio and Python 🐍')
    # Return the message to our flask website.
    return str(automatic_response)

web_app.add_url_rule('/sms', 'sms_reply', sms_reply, methods=['POST'])
# Code starts here.
if __name__ == '__main__':
    # Run this app on our localhost.
    web_app.run()
