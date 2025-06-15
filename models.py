# models.py
from datetime import datetime
from flask_sqlalchemy import SQLAlchemy
from flask_login import UserMixin
from passlib.hash import bcrypt_sha256

db = SQLAlchemy()

class User(UserMixin, db.Model):
    id           = db.Column(db.Integer, primary_key=True)
    email        = db.Column(db.String(120), unique=True, nullable=False)
    password_hash= db.Column(db.String(128), nullable=False)
    created_at   = db.Column(db.DateTime, default=datetime.utcnow)

    def set_password(self, password: str):
        self.password_hash = bcrypt_sha256.hash(password)

    def check_password(self, password: str) -> bool:
        return bcrypt_sha256.verify(password, self.password_hash)
