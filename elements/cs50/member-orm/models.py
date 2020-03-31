from flask_sqlalchemy import SQLAlchemy 

db = SQLAlchemy()

class Member(db.model):
    __tablename__ = 'member'
    id = db.Column(db.Integer, primary_key=True)
    first_name = db.Column(db.String, nullable=False)
    last_name = db.Colum(db.String, nullable=False)