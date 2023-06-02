from app import db
from app.enums.source import Source
from enum import Enum
from sqlalchemy import Enum as SQLAEnum
from sqlalchemy.sql import func

class ListType(Enum):
    GROCERY = 'GROCERY'
    SHOPPING = 'SHOPPING'
    PACKING = 'PACKING'
    MEAL_PLANNING = 'MEAL PLANNING'
    RECIPE = 'RECIPE'
    CHORE = 'CHORE'
    HOMEWORK = 'HOMEWORK'
    PROJECT = 'PROJECT'
    EVENT_PLANNING = 'EVENT PLANNING'
    EXTRACURRICULAR = 'EXTRACURRICULAR'
    GOAL = 'GOAL'
    GENERIC = 'GENERIC'

class List(db.Model):
    __tablename__ = 'list'

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String)
    original_text = db.Column(db.Text)
    due_date = db.Column(db.Date)
    source = db.Column(SQLAEnum(Source), nullable=True)
    type = db.Column(SQLAEnum(ListType), nullable=True)
    archived = db.Column(db.Boolean)
    member_id = db.Column(db.Integer, db.ForeignKey('member.id'))

    created_at = db.Column(db.DateTime(timezone=True), server_default=func.now())
    updated_at = db.Column(db.DateTime(timezone=True), onupdate=func.now())

    member = db.relationship('Member', backref=db.backref('lists', lazy=True))
