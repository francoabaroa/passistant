from app import db
from sqlalchemy import Enum as SQLAEnum
from enum import Enum

class Source(Enum):
    SMS = 'sms'
    EMAIL = 'email'
    CALENDAR = 'calendar'
    VOICE_NOTE = 'voice note'
    IMAGE = 'image'

class Priority(Enum):
    NONE = 'none'
    HIGH = 'high'

class Type(Enum):
    TASK = 'task'
    EVENT = 'event'
    APPOINTMENT = 'appointment'
    ANNIVERSARY = 'anniversary'
    BILL = 'bill'
    CHORE = 'chore'
    MEDICATION = 'medication'
    EXERCISE = 'exercise'
    HOMEWORK = 'homework'
    MEETING = 'meeting'
    GENERIC = 'generic'

class Reminder(db.Model):
    __tablename__ = 'reminder'

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String)
    details = db.Column(db.Text)
    original_text = db.Column(db.Text)
    due_date = db.Column(db.DateTime)
    start_date = db.Column(db.DateTime)
    source = db.Column(SQLAEnum(Source), nullable=True)
    completed = db.Column(db.Boolean)
    completion_date = db.Column(db.DateTime)
    priority = db.Column(SQLAEnum(Priority), nullable=True)
    type = db.Column(SQLAEnum(Type), nullable=True)
    archived = db.Column(db.Boolean)
    member_id = db.Column(db.Integer, db.ForeignKey('member.id'))

    member = db.relationship('Member', backref=db.backref('reminders', lazy=True))
