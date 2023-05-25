from flask import Blueprint, request
from twilio.twiml.messaging_response import MessagingResponse

# app = Flask(__name__)
sms_blueprint = Blueprint('sms_blueprint', __name__)

@sms_blueprint.route("/sms", methods=['POST'])
def sms_reply():
    """Respond to incoming calls with a simple text message."""
    resp = MessagingResponse()

    msg = request.form.get('Body')  # Extract the message body from the incoming request.
    resp.message("You said: {}".format(msg))
    print(msg)
    return str(resp)

