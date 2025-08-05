import os
from .base import BaseConfig

class DevelopmentConfig(BaseConfig):
    """Development configuration"""
    DEBUG = True
    TESTING = False
    # Override security for development 
    SESSION_COOKIE_SECURE = False
    REMEMBER_COOKIE_SECURE = False

    #Delvelopment specifc database
    SQLALCHEMY_DATABASE_URI = os.getenv(
        'DATABASE_URL',
        'postgresql://localhost/inventory_dev_db'
    )