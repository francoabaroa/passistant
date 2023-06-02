from app.models import List, Member, Reminder
from app import db
from sqlalchemy import and_

class DataRetrievalService:
    def __init__(self):
        pass

    def get_all_list_names(self, from_number):
        lists = db.session.query(List).join(Member).filter(
            and_(Member.phone == from_number, List.member_id == Member.id)
        ).all()

        all_lists = [
            {
                'name': list.name,
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
