class DataProcessingService:
    def __init__(self):
        pass

    def process_text(self, msg):
        # Your text processing code goes here
        print("Processing text: {}".format(msg))

    def process_audio(self, media_url):
        # Your audio processing code goes here
        print("Processing audio from: {}".format(media_url))

    def process_image(self, media_url):
        # Your image processing code goes here
        print("Processing image from: {}".format(media_url))

    def process_document(self, media_url):
        # Your document processing code goes here
        print("Processing document from: {}".format(media_url))

    def process_unsupported(self, media_url):
        # Code to handle unsupported media types goes here
        print("Cannot process unsupported file type from: {}".format(media_url))
