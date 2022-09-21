from datetime import date

from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()

class User(db.Model):
    __tablename__ = "users"
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    email = db.Column(db.String(50), nullable=False, unique=True)
    username = db.Column(db.String(50), nullable=False)
    password = db.Column(db.String(50), nullable=False)
    is_admin = db.Column(db.Boolean, nullable=False)
    date_added = db.Column(db.Date())

    def __init__(self, email: str, username: str, password: str,
                 is_admin: bool = False, date_added: date = None):
        self.email = email
        self.username = username
        self.password = password
        self.is_admin = is_admin
        self.date_added = date_added

    def __repr__(self):
        return f"User(id={self.id!r}, username={self.username!r}, email={self.email!r})"