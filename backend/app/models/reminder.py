from app import db
from sqlalchemy import Enum as SQLAEnum
from enum import Enum

class Source(Enum):
    SMS = 'SMS'
    EMAIL = 'EMAIL'
    CALENDAR = 'CALENDAR'
    VOICE_NOTE = 'VOICE NOTE'
    IMAGE = 'IMAGE'

class Priority(Enum):
    NONE = 'NONE'
    HIGH = 'HIGH'

class Type(Enum):
    TASK = 'TASK'
    EVENT = 'EVENT'
    APPOINTMENT = 'APPOINTMENT'
    ANNIVERSARY = 'ANNIVERSARY'
    BILL = 'BILL'
    CHORE = 'CHORE'
    MEDICATION = 'MEDICATION'
    EXERCISE = 'EXERCISE'
    HOMEWORK = 'HOMEWORK'
    MEETING = 'MEETING'
    GENERIC = 'GENERIC'

class Reminder(db.Model):
    __tablename__ = 'reminder'

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String)
    details = db.Column(db.Text)
    original_text = db.Column(db.Text)
    due_date = db.Column(db.Date)
    due_time = db.Column(db.Time)
    start_date = db.Column(db.DateTime)
    source = db.Column(SQLAEnum(Source), nullable=True)
    completed = db.Column(db.Boolean)
    completion_date = db.Column(db.DateTime)
    priority = db.Column(SQLAEnum(Priority), nullable=True)
    type = db.Column(SQLAEnum(Type), nullable=True)
    archived = db.Column(db.Boolean)
    member_id = db.Column(db.Integer, db.ForeignKey('member.id'))

    member = db.relationship('Member', backref=db.backref('reminders', lazy=True))
