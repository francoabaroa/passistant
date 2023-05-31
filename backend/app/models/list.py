from app import db
from sqlalchemy import Enum as SQLAEnum
from enum import Enum

class Type(Enum):
    GROCERY = 'grocery'
    SHOPPING = 'shopping'
    PACKING = 'packing'
    MEAL_PLANNING = 'meal planning'
    RECIPE = 'recipe'
    CHORE = 'chore'
    HOMEWORK = 'homework'
    PROJECT = 'project'
    EVENT_PLANNING = 'event planning'
    EXTRACURRICULAR = 'extracurricular'
    GOAL = 'goal'
    GENERIC = 'generic'

class List(db.Model):
    __tablename__ = 'list'

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String)
    original_text = db.Column(db.Text)
    due_date = db.Column(db.DateTime)
    type = db.Column(SQLAEnum(Type), nullable=True)
    archived = db.Column(db.Boolean)
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'))

    user = db.relationship('User', backref=db.backref('lists', lazy=True))
