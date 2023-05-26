import openai
import os
from os.path import basename
from pydub import AudioSegment
import requests
import re
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
            is_reminder = False
            is_list = False

            conversation = [
                {"role": "system", "content": "You are a helpful assistant. When given a piece of text, your job is to classify it as a reminder or as a list. If it's a reminder, reply in the following format 'Reminder: [reminder]'. If it's a list, reply in the following format 'List: [list]'"},
                {"role": "user", "content": msg}
            ]

            response = openai.ChatCompletion.create(
                # model="gpt-3.5-turbo",
                model="gpt-4",
                messages=conversation,
            )

            # Extract the assistant's reply
            assistant_reply = response['choices'][0]['message']['content']

            # Check if the assistant identified the text as a reminder or a list
            if 'reminder' in assistant_reply.lower():
                is_reminder = True

                # If it's a reminder, ask the assistant to identify details about the reminder
                conversation.append({
                    "role": "system",
                    "content": "You identified the text as a reminder. "
                    "Please respond with 1. reminder, 2. whether it has a due date, 3. when the due date is, "
                    "and 4. what time. Please respond in the following format: "
                    "'1. Reminder: [reminder], 2. Has due date: [Yes or No], 3. Due date: [date or None], "
                    "4. Due time: [time or None]'. It's important that you add the numbers before the responses, "
                    "such as 1. Reminder, 2. Has due date, 3. Due date, 4. Due time. "
                    "When a timeframe like 'this week' is mentioned, "
                    "please consider it as a due date for the entire week, not just the end of the week."
                })

            elif 'list' in assistant_reply.lower():
                is_list = True

                # If it's a list, ask the assistant to identify details about the list
                conversation.append({
                    "role": "system",
                    "content": "You identified the text as a list. "
                    "I need you to identify what the list name is, "
                    "what the list type is (grocery, shopping, packing, etc), "
                    "what the list items are and when the due date for the list is. "
                    "Please respond with 1. list name, 2. list type, 3. list items separated by a comma, 4. list due date. "
                    "Please respond in the following format: "
                    "'1. List name: [name] 2. List type: [type], 3. List items: [items], 4. List due date: [date or None]'. "
                    "It's important that you add the numbers before the responses, such as 1. List name, 2. List type, 3. List items, 4. List due date."
                    "When a timeframe like 'this week' is mentioned, "
                    "please consider it as a due date for the entire week, not just the end of the week."
                })

            response = openai.ChatCompletion.create(
                # model="gpt-3.5-turbo",
                model="gpt-4",
                messages=conversation,
            )

            if is_reminder:
                # Split the response into individual components.
                components = re.split(r'\d+\. ', response['choices'][0]['message']['content'])

                # Remove empty strings from the list
                components = [component for component in components if component]

                # Extract the details from the components, ensure there are enough components before proceeding
                if len(components) < 4:
                    # We should still save it and mark it as human required TRUE
                    print("Insufficient information extracted from the response.")
                    return

                reminder = components[0].split(': ')[1].strip()
                reminder = reminder[:-1] if reminder[-1] == "," else reminder

                has_due_date = components[1].split(': ')[1].strip()
                has_due_date = has_due_date[:-1] if has_due_date[-1] == "," else has_due_date

                due_date = components[2].split(': ')[1].strip()
                due_date = due_date[:-1] if due_date[-1] == "," else due_date

                time_due = components[3].split(': ')[1].strip()
                time_due = time_due[:-1] if time_due[-1] == "," else time_due

                # TODO: implement formatted due_date and time
                reminder_dict = {
                    "original_text": msg,
                    "reminder": reminder,
                    "has_due_date": has_due_date,
                    "due_date": due_date,
                    "formatted_due_date": '',
                    "time_due": time_due,
                    "formatted_time": ''
                }

            elif is_list:
                # Split the response into individual components.
                components = re.split(r'\d+\. ', response['choices'][0]['message']['content'])

                # Remove empty strings from the list
                components = [component for component in components if component]

                # Extract the details from the components, ensure there are enough components before proceeding
                if len(components) < 4:
                    # We should still save it and mark it as human required TRUE
                    print("Insufficient information extracted from the response.")
                    return

                name = components[0].split(': ')[1].strip()
                name = name[:-1] if name[-1] == "," else name

                type = components[1].split(': ')[1].strip()
                type = type[:-1] if type[-1] == "," else type

                items = components[2].split(': ')[1].strip()
                items = items[:-1].lower() if items[-1] == "," else items.lower()

                formatted_items = items.split(', ')

                time_due = components[3].split(': ')[1].strip()
                time_due = time_due[:-1] if time_due[-1] == "," else time_due

                # TODO: implement formatted due_date and time
                list_dict = {
                    "original_text": msg,
                    "name": name,
                    "type": type,
                    "items": items,
                    "formatted_items": formatted_items,
                    "time_due": time_due,
                    "formatted_time": ''
                }

            if is_reminder: return reminder_dict
            if is_list: return list_dict
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
            print("\033[96m\033[1m"+"\n*****transcript_end*****\n"+"\033[0m\033[0m")

            # Process transcript
            processed_text = self.process_text(transcript.text)

            # Remove the original and converted audio files
            os.remove(filename)
            os.remove(converted_filename)

            return processed_text

        print("Processing audio from: {}".format(media_url))

    def process_image(self, media_url):
        # Your image processing code goes here
        # examples: birthday invitation
        # examples: whiteboard screenshot?
        # Use gpt3.5 to store safely in database
        # Steps
        # What will you use to parse image?
        # https://huggingface.co/docs/transformers/model_doc/trocr
        # Tesseract OCR
        # Amazon Textract
        print("Processing image from: {}".format(media_url))

    def process_document(self, media_url):
        # Use gpt3.5 to store safely in database
        # Your document processing code goes here
        print("Processing document from: {}".format(media_url))

    def process_unsupported(self, media_url):
        # Use gpt3.5 to store safely in database
        # Code to handle unsupported media types goes here
        print("Cannot process unsupported file type from: {}".format(media_url))
