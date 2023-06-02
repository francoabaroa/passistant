from app import db
from app.enums.source import Source
from enum import Enum
from sqlalchemy import Enum as SQLAEnum
from sqlalchemy.sql import func

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

    created_at = db.Column(db.DateTime(timezone=True), server_default=func.now())
    updated_at = db.Column(db.DateTime(timezone=True), onupdate=func.now())

    member = db.relationship('Member', backref=db.backref('reminders', lazy=True))
