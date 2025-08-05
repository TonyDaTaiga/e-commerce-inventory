import os
from dotenv import load_dotenv

# load environment variables from .env file
load_dotenv()

from .development import DevelopmentConfig
from .production import ProductionConfig
from .testing import TestingConfig

# Dictionary to map config names to config classes
config_by_name = {
    'development': DevelopmentConfig,
    'testing': TestingConfig,
    'production': ProductionConfig,
    'default': DevelopmentConfig
}

def get_config(config_name):
    """Helper function to get config by name"""
    return config_by_name.get(config_name, DevelopmentConfig)