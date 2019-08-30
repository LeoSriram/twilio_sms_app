# Import Twilio.
from twilio.rest import Client
# Import required hidden numbers from other file.
from my_secret_numbers import Cell_number, AUTH_TOKEN
# Import the flask framework
from flask import Flask
# This is required to respont to texts that come in.
from twilio.twiml.messaging_response import MessagingResponse
# Import pandas package.
import pandas as pd

# Codes required by twilio.
ACCOUNT_SID = 'ACaa49420ab61ad5584d34556236d5c326'
auth_token = AUTH_TOKEN

# Make our twilio client.
client = Client(ACCOUNT_SID, auth_token)
# Numbers of sender and reciever
sender = '+12562428054'
numbers = pd.read_csv('numbers.csv', names=['Phone']).phone.to_list()[1:]
blacklist = pd.read_csv('blacklist.csv', names=['Phone']).phone.to_list()[1:]
recievers = list(set(numbers).difference(set(blacklist)))

def broadcast():
    # To add time delay feature, uncomment the below code.
    #import time
    #time.sleep(100)

    for reciever in recievers:
        # The text going to be sent out.
        text = '\n\nHey There subscriber! Do you want to make different loom bands?' + \
               '\n\n Reply Y to Get the link.' + \
               '\n\nReply B to be blacklisted.'
        # Use the client to send the SMS text.
        client.messages.create(to=reciever, from_=sender, body=text)


# Create our flask app
web_app = Flask(__name__)

def sms_reply():

    if request.method == 'POST':
        # Getting the incoming data from the subscriber.
        number = request.form['From']
        message_body = request.form['Body']
        # If they reply Y.
        if message_body == 'Y':
            response_text = 'https://www.youtube.com/watch?v=3dfJE912vpQ'
        # If they reply B.
        if message_body == 'B':
            blacklist.append(number)
            df = pd.DataFrame('blacklist', columns=['Phone'])
            df.to_csv('blacklist.csv', index=False)
            response_text = 'You have been blacklisted.'

    # Create a response object.
    automatic_response = MessagingResponse()
    # Put a message in our response object.
    automatic_response.message(response_text)
    # Return the message to our flask website.
    return str(automatic_response)

web_app.add_url_rule('/sms', 'sms_reply', sms_reply, methods=['POST'])
# Code starts here.
if __name__ == '__main__':
    # Run this app on our localhost.
    web_app.run()
    broadcast()
