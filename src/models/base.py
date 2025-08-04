from datetime import datetime
from src import db

class BaseModel(db.Model):
    """Base model class with common fields"""
    __abstract__ = True

    id = db.Column(db.Integer, primary_key=True)
    created_at = db.Column(db.DateTime, default=datetime.now(datetime.timezone.jst))
    updated_at = db.Column(db.DateTime, default=datetime.now(datetime.timezone.jst), onupdate=datetime.now(datetime.timezone.jst))

    def save(self):
        """save model instance to db"""
        db.session.add(self)
        db.session.commit()

    def delete(self):
        """delete model instance from db"""
        db.session.delete(self)
        db.session.commit()

    @classmethod
    def get_by_id(cls, id):
        """get model instance by ID"""
        return cls.query.get(id)