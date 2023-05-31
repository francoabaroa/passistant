from app import db
from sqlalchemy import Enum as SQLAEnum
from enum import Enum

class Role(Enum):
    PARENT = 'parent'
    FAMILY = 'family'
    CAREGIVER = 'caregiver'

class Status(Enum):
    ACTIVE = 'active'
    INACTIVE = 'inactive'
    DELETED = 'deleted'

class User(db.Model):
    __tablename__ = 'user'

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(64))
    # TODO: need to validate email
    email = db.Column(db.String(120), unique=True)
    # TODO: need to validate email
    phone = db.Column(db.String)
    phone_country_code = db.Column(db.String)
    role = db.Column(SQLAEnum(Role), nullable=True)
    password_hash = db.Column(db.String)
    provider = db.Column(db.String)
    provider_id = db.Column(db.String)
    status = db.Column(SQLAEnum(Status), nullable=True)
    timezone = db.Column(db.String)
    family_id = db.Column(db.Integer, db.ForeignKey('family.id'))

    family = db.relationship('Family', backref=db.backref('users', lazy=True))
