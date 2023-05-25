from flask import request
from twilio.twiml.messaging_response import MessagingResponse

class DataIngestionService:
    def ingest_sms(self):
        resp = MessagingResponse()
        msg = request.form.get('Body')  # Extract the message body from the incoming request.
        media_type = request.form.get('MediaContentType0')  # Extract the media type from the incoming request.
        media_url = request.form.get('MediaUrl0')  # Extract the media URL from the incoming request.

        if media_type is None:
            response_text = "You sent a text message: {}".format(msg)
        elif 'audio' in media_type:
            response_text = "You sent a voice note: {}".format(media_url)
        elif 'image' in media_type:
            response_text = "You sent an image: {}".format(media_url)
        elif 'application/pdf' in media_type:
            response_text = "You sent a PDF: {}".format(media_url)
        else:
            response_text = "You sent an unsupported file type: {}".format(media_url)

        resp.message(response_text)
        print(response_text)
        return str(resp)