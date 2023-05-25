import openai
import os

from dotenv import load_dotenv

load_dotenv()
openai.api_key = os.getenv("OPENAI_API_KEY", "")

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
