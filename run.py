from src import create_app
from config import get_config
import os

#get config name from environment variable or default to 'development'
config_name = os.getenv('FLASK_CONFIG', 'development')
app = create_app(get_config(config_name))

if __name__ == '__main__':
    app.run()