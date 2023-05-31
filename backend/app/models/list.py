from app import db
from sqlalchemy import Enum as SQLAEnum
from enum import Enum

class Type(Enum):
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
    due_date = db.Column(db.DateTime)
    type = db.Column(SQLAEnum(Type), nullable=True)
    archived = db.Column(db.Boolean)
    member_id = db.Column(db.Integer, db.ForeignKey('member.id'))

    member = db.relationship('Member', backref=db.backref('lists', lazy=True))
