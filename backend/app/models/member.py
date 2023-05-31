from app import db
from sqlalchemy import Enum as SQLAEnum
from enum import Enum

class Role(Enum):
    PARENT = 'PARENT'
    FAMILY = 'FAMILY'
    CAREGIVER = 'CAREGIVER'

class Status(Enum):
    ACTIVE = 'ACTIVE'
    INACTIVE = 'INACTIVE'
    DELETED = 'DELETED'

class Member(db.Model):
    __tablename__ = 'member'

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(64))
    # TODO: need to validate email
    email = db.Column(db.String(120), unique=True)
    # TODO: need to validate phone
    phone = db.Column(db.String)
    phone_country_code = db.Column(db.String)
    role = db.Column(SQLAEnum(Role), nullable=True)
    password_hash = db.Column(db.String)
    provider = db.Column(db.String)
    provider_id = db.Column(db.String)
    status = db.Column(SQLAEnum(Status), nullable=True)
    timezone = db.Column(db.String)
    family_id = db.Column(db.Integer, db.ForeignKey('family.id'))

    family = db.relationship('Family', backref=db.backref('members', lazy=True))