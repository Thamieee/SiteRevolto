from datetime import datetime, date

from flask_sqlalchemy import SQLAlchemy
from flask_login import UserMixin

db = SQLAlchemy()

# class User(db.Model):
#     __tablename__ = "users"
#     id = db.Column(db.Integer, primary_key=True, autoincrement=True)
#     email = db.Column(db.String(50), nullable=False, unique=True)
#     username = db.Column(db.String(50), nullable=False, unique=True)
#     password = db.Column(db.String(50), nullable=False)
#     is_admin = db.Column(db.Boolean, nullable=False)
#     is_confirmed = db.Column(db.Boolean, nullable=False)
#     date_added = db.Column(db.Date())
#     confirmed_on = db.Column(db.Date())
#
#     def __init__(self, email: str, username: str, password: str,
#                  is_admin: bool = False, is_confirmed: bool = False,
#                  date_added: date = None, confirmed_on: datetime = None):
#         self.email = email
#         self.username = username
#         self.password = password
#         self.is_admin = is_admin
#         self.is_confirmed = is_confirmed
#         self.date_added = date_added
#         self.confirmed_on = confirmed_on
#
#     def __repr__(self):
#         return f"User(id={self.id!r}, username={self.username!r}, email={self.email!r})"

class User(UserMixin, db.Model):
    id = db.Column(db.Integer, primary_key=True) # primary keys are required by SQLAlchemy
    email = db.Column(db.String(100), unique=True)
    password = db.Column(db.String(100))
    name = db.Column(db.String(1000))