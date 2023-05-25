import openai
import os
from os.path import basename
from pydub import AudioSegment
import requests
from requests.auth import HTTPBasicAuth
from urllib.parse import urlparse

from dotenv import load_dotenv

load_dotenv()
openai.api_key = os.getenv("OPENAI_API_KEY", "")
account_sid = os.getenv("TWILIO_ACCOUNT_SID", "")
auth_token = os.getenv("TWILIO_AUTH_TOKEN", "")

class DataProcessingService:
    def __init__(self):
        pass

    def process_text(self, msg):
        try:
            print(f"Processing text: {msg}")

            messages=[
                {"role": "system", "content": "You are a helpful assistant. When asked a task and time, your job is to identify and respond with the task, whether it has a deadline, and if so, when the deadline is, in the following format: '1. Task: [task], 2. Deadline: [Yes or No], 3. When: [time or Null]'"},
                {"role": "user", "content": msg},
            ]

            response = openai.ChatCompletion.create(
                model="gpt-3.5-turbo",
                messages=messages,
                temperature=0.3,
                max_tokens=150
            )

            response_content = response.choices[0].message.content.strip()
            print(f"Response content: {response_content}")

            # Split the response into individual components.
            components = response_content.split(',')

            # Extract the details from the components, ensure there are enough components before proceeding
            if len(components) < 3:
                print("Insufficient information extracted from the response.")
                return

            task = components[0].split(': ')[1].strip()
            has_deadline = components[1].split(': ')[1].strip()
            deadline = components[2].split(': ')[1].strip()

            response_format = f"1. Task: {task}\n2. Deadline: {has_deadline}\n3. When: {deadline}"
            print(response_format)

            # Create the dictionary.
            task_dict = {
                "message": msg,
                "task": task,
                "has_deadline": has_deadline,
                "deadline": deadline
            }

            print(task_dict)
            return task_dict
        except Exception as e:
            print(f"Error in process_text: {str(e)}")
            return None

    def process_audio(self, media_url):
        parsed = urlparse(media_url)
        filename = basename(parsed.path)

        # Retrieve the file from the url
        response = requests.get(media_url, stream=True, auth=HTTPBasicAuth(account_sid, auth_token))
        if response.status_code == 200:
            with open(filename, 'wb') as audio_file:
                for chunk in response.iter_content(chunk_size=1024):
                    if chunk:
                        audio_file.write(chunk)

            # Convert the audio file to a supported format for OpenAI Whisper
            filename_without_ext = os.path.splitext(filename)[0]
            converted_filename = filename_without_ext + ".wav"

            audio = AudioSegment.from_file(filename)
            audio.export(converted_filename, format="wav")

            with open(converted_filename, "rb") as audio_file:
                transcript = openai.Audio.transcribe("whisper-1", audio_file)

            print("\033[96m\033[1m"+"\n*****transcript*****\n"+"\033[0m\033[0m")
            print(transcript.text)

            # Process transcript
            self.process_text(transcript.text)

            # Remove the original and converted audio files
            os.remove(filename)
            os.remove(converted_filename)

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
