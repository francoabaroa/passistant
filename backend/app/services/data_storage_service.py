# Handle and store data
# Save data to calendar/todo
# make sure to validate phone and email
from app.models import Member, Family, Reminder
from app.models.reminder import Priority, Source, Type
from app import db
from datetime import datetime

# TODO: use phone number to look up member.id
TEMP_HARDCODED_ID = 1

class DataStorageService:
    def __init__(self):
        pass

    def store_data(self, data):
        # Stub function to simulate data storing
        print("Storing data: ", data)
        return data

    def store_list(self, data):
        print('')

    def store_reminder(self, data, original_text, source):
        reminder_content = data.get('reminderContent', {})
        formatted_due_time = reminder_content.get('formattedDueTime')

        if formatted_due_time is not None:
            formatted_due_time = datetime.strptime(formatted_due_time, '%H:%M').time()

        new_reminder = Reminder(
            name          = reminder_content.get('reminderName'),
            details       = reminder_content.get('reminderDetails'),
            due_date      = reminder_content.get('formattedDueDate'),
            priority      = Priority(reminder_content.get('priority').upper()),
            type          = Type(reminder_content.get('reminderType').upper()),
            due_time      = formatted_due_time,
            source        = Source(source.upper()),
            original_text = original_text,
            member_id     = TEMP_HARDCODED_ID
        )

        db.session.add(new_reminder)
        db.session.commit()
        print('Saved Reminder')

