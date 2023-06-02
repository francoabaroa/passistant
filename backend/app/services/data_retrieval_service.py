from app.models import List, Member, Reminder
from app import db
from sqlalchemy import and_

class DataRetrievalService:
    def __init__(self):
        pass

    def get_all_lists(self, from_number):
        lists = db.session.query(List).join(Member).filter(
            and_(Member.phone == from_number, List.member_id == Member.id)
        ).all()

        all_lists = [
            {
                'name': list.name,
                'items': [{'name': item.name, 'quantity': item.quantity} for item in list.list_items]
            }
            for list in lists
        ]

        return all_lists

    def get_all_reminder_names(self, from_number):
        reminders = db.session.query(Reminder).join(Member).filter(
            and_(Member.phone == from_number, Reminder.member_id == Member.id)
        ).all()

        all_reminders = [
            {
                'name': reminder.name,
            }
            for reminder in reminders
        ]

        return all_reminders
