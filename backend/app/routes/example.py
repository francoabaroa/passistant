from flask import Blueprint, jsonify
from twilio.rest import Client
from dotenv import load_dotenv
import os

load_dotenv()
TWILIO_ACCOUNT_SID = os.getenv("TWILIO_ACCOUNT_SID", "")
TWILIO_AUTH_TOKEN = os.getenv("TWILIO_AUTH_TOKEN", "")
TWILIO_TO_NUMBER = os.getenv("TWILIO_TO_NUMBER", "")
TWILIO_FROM_NUMBER = os.getenv("TWILIO_FROM_NUMBER", "")

example = Blueprint('example', __name__)

@example.route('/')
def hello_world():
    send_sms()
    return jsonify({"message": "Hello, World!"})

def send_sms():
    account_sid = TWILIO_ACCOUNT_SID
    auth_token = TWILIO_AUTH_TOKEN
    client = Client(account_sid, auth_token)

    message = client.messages.create(
        to=TWILIO_TO_NUMBER,
        from_=TWILIO_FROM_NUMBER,
        body="Hello from Python!")

    print(message.sid)

