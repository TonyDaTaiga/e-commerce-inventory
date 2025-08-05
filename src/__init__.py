from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_login import LoginManager
from flask_migrate import Migrate

#initize extensions
db = SQLAlchemy()
login_manager = LoginManager()
migrate = Migrate()

def create_app(config_object):
    """application factory function"""
    app = Flask(__name__)
    app.config.from_object(config_object)

    #initilize extensions with app
    db.init_app(app)
    login_manager.init_app(app)
    migrate.init_app(app, db)

    # import and register blueprints
    from src.routes import auth_routes, product_routes, order_routes
    app.register_blueprint(auth_routes.bp)
    app.register_blueprint(product_routes.bp)
    app.register_blueprint(order_routes.bp)

    return app