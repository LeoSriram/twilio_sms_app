# Import the flask framework
from flask import Flask
# This is required to respont to texts that come in.
from twilio.twiml.messaging_response import MessagingResponse

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
