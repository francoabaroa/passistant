from app import db
from sqlalchemy.sql import func

class ListItem(db.Model):
    __tablename__ = 'list_item'

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String)
    # quantity is string because sometimes gpt4 will return a string like '2 dozens' or 1
    quantity = db.Column(db.String)
    completed = db.Column(db.Boolean)
    favorited = db.Column(db.Boolean)
    list_id = db.Column(db.Integer, db.ForeignKey('list.id'))

    created_at = db.Column(db.DateTime(timezone=True), server_default=func.now())
    updated_at = db.Column(db.DateTime(timezone=True), onupdate=func.now())

    list = db.relationship('List', backref=db.backref('list_items', lazy=True))
