from app import db

class Family(db.Model):
    __tablename__ = 'family'

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(64), nullable=False)