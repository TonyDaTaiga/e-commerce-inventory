from werkzeug.security import generate_password_hash, check_password_hash
from flask_login import UserMixin
from src import db
from .base import BaseModel

class User(BaseModel, UserMixin):
    """User model for authentication and authorization"""
    __tablename__ = 'users'

    email = db.Column(db.String(120), unique=True, nullable=False)
    username = db.Column(db.String(80), unique=True, nullable=False)
    password_hash = db.Column(db.String(255), nullable=False)
    is_active = db.Column(db.Boolean, default=True)
    is_admin =db.Column(db.Boolean, default=False)

    def set_password(self, password):
        """Set password hash"""
        self.password_hash = generate_password_hash(password)

    def check_password(self, password):
        """check password against hash"""
        return check_password_hash(self.password_hash, password)
    
@classmethod
def get_by_email(cls, email):
    """Get user by email"""
    return cls.query.filter_by(email=email).first()

def __repr__(self):
    return f'<User {self.username}>'