from flask import request
from twilio.twiml.messaging_response import MessagingResponse
from .data_processing_service import DataProcessingService

class DataIngestionService:
    def __init__(self):
        self.data_processor = DataProcessingService()

    def ingest_sms(self):
        resp = MessagingResponse()
        msg = request.form.get('Body')  # Extract the message body from the incoming request.
        media_type = request.form.get('MediaContentType0')  # Extract the media type from the incoming request.
        media_url = request.form.get('MediaUrl0')  # Extract the media URL from the incoming request.

        if media_type is None:
            response_text = "You sent a text message: {}".format(msg)
            self.data_processor.process_text(msg)
        elif 'audio' in media_type:
            response_text = "You sent a voice note: {}".format(media_url)
            self.data_processor.process_audio(media_url)
        elif 'image' in media_type:
            response_text = "You sent an image: {}".format(media_url)
            self.data_processor.process_image(media_url)
        elif 'application/pdf' in media_type:
            response_text = "You sent a PDF: {}".format(media_url)
            self.data_processor.process_document(media_url)
        else:
            response_text = "You sent an unsupported file type: {}".format(media_url)
            self.data_processor.process_unsupported(media_url)

        resp.message(response_text)
        print(response_text)
        return str(resp)