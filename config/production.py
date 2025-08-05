import os
from .base import BaseConfig

class ProductionConfig(BaseConfig):
    """Production configuration"""
    DEBUG = False
    TESTING = False
    
    #production database 
    SQLALCHEMY_DATABASE_URI = os.getenv('DATABASE_URL')

    #production security
    SESSION_COOKIE_SECURE = True
    REMEMBER_COOKIE_SECURE = True