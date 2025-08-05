from .base import BaseConfig

class TestingConfig(BaseConfig):
    """Testing configureation"""
    TESTING = True
    DEBUG = False
    
    # use in moroy sqlite for tests
    SQLALCHEMY_DATABASE_URI = 'sqlite:///:memory:'

    #disable csrf tokens in testing 
    WTF_CSRF_ENABLED = False