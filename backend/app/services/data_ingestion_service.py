from flask import request, jsonify
from twilio.twiml.messaging_response import MessagingResponse
from twilio.rest import Client
from .data_processing_service import DataProcessingService
from dotenv import load_dotenv
import os

load_dotenv()
TWILIO_ACCOUNT_SID = os.getenv("TWILIO_ACCOUNT_SID", "")
TWILIO_AUTH_TOKEN = os.getenv("TWILIO_AUTH_TOKEN", "")
TWILIO_TO_NUMBER = os.getenv("TWILIO_TO_NUMBER", "")
TWILIO_FROM_NUMBER = os.getenv("TWILIO_FROM_NUMBER", "")

class DataIngestionService:
    def __init__(self):
        self.data_processor = DataProcessingService()

    def ingest_sms(self):
        resp = MessagingResponse()
        msg = request.form.get('Body')  # Extract the message body from the incoming request.
        media_type = request.form.get('MediaContentType0')  # Extract the media type from the incoming request.
        media_url = request.form.get('MediaUrl0')  # Extract the media URL from the incoming request.

        if media_type is None:
            response = self.data_processor.process_text(msg)
            self.send_response_sms(response)
        elif 'audio' in media_type:
            response = self.data_processor.process_audio(media_url)
            self.send_response_sms(response)
        elif 'image' in media_type:
            response = self.data_processor.process_image(media_url)
            self.send_response_sms(response)
        elif 'application/pdf' in media_type:
            response = "You sent a PDF: {}".format(media_url)
            self.data_processor.process_document(media_url)
        else:
            response = "You sent an unsupported file type: {}".format(media_url)
            self.data_processor.process_unsupported(media_url)

        resp.message(response)
        return str(resp)

    def send_response_sms(self, body):
        account_sid = TWILIO_ACCOUNT_SID
        auth_token = TWILIO_AUTH_TOKEN
        client = Client(account_sid, auth_token)

        message = client.messages.create(
            to=TWILIO_TO_NUMBER,
            from_=TWILIO_FROM_NUMBER,
            body=body)

        print(message.sid)