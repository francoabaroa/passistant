from flask import Blueprint, jsonify
from twilio.rest import Client
from dotenv import load_dotenv
import os
from app import db

from app.models import Reminder, List, Member

load_dotenv()

# TODO: Temporary,
TWILIO_TO_NUMBER = os.getenv("TWILIO_TO_NUMBER", "")

api = Blueprint('api', __name__)

@api.route('/')
def hello_world():
    return jsonify({"message": "Hello, World!"})

# TODO: get_all_reminders and get_all_lists should be in a separate data_query_service
@api.route('/api/reminders', methods=['GET'])
def get_all_reminders():
    reminders = db.session.query(Reminder).join(Member).filter(Member.phone == TWILIO_TO_NUMBER).all()
    all_reminders = [
        {
            'id': reminder.id,
            'name': reminder.name,
            'details': reminder.details,
            'original_text': reminder.original_text,
            'due_date': reminder.due_date.isoformat() if reminder.due_date else None,
            'due_time': reminder.due_time.isoformat() if reminder.due_time else None,
            'start_date': reminder.start_date.isoformat() if reminder.start_date else None,
            'source': reminder.source.name if reminder.source else None,
            'completed': reminder.completed,
            'completion_date': reminder.completion_date.isoformat() if reminder.completion_date else None,
            'priority': reminder.priority.name if reminder.priority else None,
            'type': reminder.type.name if reminder.type else None,
            'archived': reminder.archived,
            'member_id': reminder.member_id
        }
        for reminder in reminders
    ]
    return jsonify(all_reminders)

@api.route('/api/lists', methods=['GET'])
def get_all_lists():
    lists = db.session.query(List).join(Member).filter(Member.phone == TWILIO_TO_NUMBER).all()
    all_lists = [
        {
            'id': list.id,
            'name': list.name,
            'original_text': list.original_text,
            'due_date': list.due_date.isoformat() if list.due_date else None,
            'type': list.type.name if list.type else None,
            'archived': list.archived,
            'member_id': list.member_id,
            'list_items': [
                {
                    'id': item.id,
                    'name': item.name,
                    'quantity': item.quantity,
                    'completed': item.completed,
                    'favorited': item.favorited
                }
                for item in list.list_items
            ]
        }
        for list in lists
    ]
    return jsonify(all_lists)
