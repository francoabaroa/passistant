# Save data to calendar/todo
# make sure to validate phone and email
from app.models import List, ListItem, Reminder
from app.models.reminder import Priority, Type
from app.enums.source import Source
from app.models.list import ListType
from app import db
from datetime import datetime

# TODO: use phone number to look up member.id
TEMP_HARDCODED_ID = 1

class DataStorageService:
    def __init__(self):
        pass

    def store_list(self, data, original_text, source):
        list_content = data.get('listContent', {})
        list_items = list_content.get('listItems')

        new_list = List(
            name          = list_content.get('listName'),
            due_date      = list_content.get('formattedDueDate'),
            type          = ListType(list_content.get('listType').upper()),
            source        = Source(source.upper()),
            original_text = original_text,
            member_id     = TEMP_HARDCODED_ID
        )

        db.session.add(new_list)
        db.session.commit()

        items = [ListItem(name=name, quantity=str(quantity), completed=False, favorited=False, list_id=new_list.id) for name, quantity in list_items.items()]

        db.session.add_all(items)
        db.session.commit()
        print('Saved List')

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

