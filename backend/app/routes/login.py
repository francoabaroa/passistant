from flask import Blueprint, request, session, jsonify
import re
from twilio.rest import Client
import random
import hashlib
from dotenv import load_dotenv
import os

load_dotenv()

TWILIO_ACCOUNT_SID = os.getenv("TWILIO_ACCOUNT_SID", "")
TWILIO_AUTH_TOKEN = os.getenv("TWILIO_AUTH_TOKEN", "")
TWILIO_TO_NUMBER = os.getenv("TWILIO_TO_NUMBER", "")
TWILIO_FROM_NUMBER = os.getenv("TWILIO_FROM_NUMBER", "")

login_blueprint = Blueprint('login_blueprint', __name__)

@login_blueprint.route('/login', methods=['POST'])
def login():
    # TODO: Implement
    print('login')

@login_blueprint.route('/send_code', methods=['POST'])
def send_code():
    data = request.get_json()
    email_or_phone = data.get('email_or_phone')
    code = random.randint(100000, 999999)
    hashed_code = hashlib.sha256(str(code).encode()).hexdigest()

    # store email or phone number and hashed code in session
    session['email_or_phone'] = email_or_phone
    session['code'] = hashed_code

    if re.match(r'^\+?\d{9,15}$', email_or_phone):  # phone number
        account_sid = TWILIO_ACCOUNT_SID
        auth_token = TWILIO_AUTH_TOKEN
        client = Client(account_sid, auth_token)
        client.messages.create(
            body=f'Your verification code is: {code}',
            from_=TWILIO_FROM_NUMBER,
            to=email_or_phone
        )
        print('Code sent')
    else:  # email
        # TODO: Implement
        print('send_email_code')


    return jsonify({"message": "Code sent"})

@login_blueprint.route('/verify_code', methods=['POST'])
def verify_code():
    data = request.get_json()
    user_code = data.get('code')
    hashed_user_code = hashlib.sha256(str(user_code).encode()).hexdigest()

    if 'email_or_phone' in session and 'code' in session:
        if session['code'] == hashed_user_code:
            # user is verified, handle accordingly
            return jsonify({"message": "User verified"})
        else:
            return jsonify({"message": "Invalid code"}), 401
    else:
        return jsonify({"message": "No code sent"}), 400

@login_blueprint.route('/google_login', methods=['POST'])
def google_login():
    # TODO: Implement
    auth_code = request.form.get('auth_code')

    # user_info = get_google_user_info(auth_code)

    # handle user authentication and registration using user_info
    # ...

    return jsonify({"message": "User authenticated"})
