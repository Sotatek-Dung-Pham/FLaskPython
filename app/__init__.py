from flask import Flask, render_template
from flask_sqlalchemy import SQLAlchemy
from flask_jwt_extended import JWTManager
from flask_bcrypt import Bcrypt
from flask_migrate import Migrate
from config import app_config
from flask_login import LoginManager

app = Flask(__name__, instance_relative_config = True, template_folder = '../templates', static_url_path = '', static_folder = '../static')
db = SQLAlchemy()
bcrypt = Bcrypt()
migrate = Migrate()
login_manager = LoginManager()

def create_app(config_name):
    app.config.from_object(app_config[config_name])
    jwt = JWTManager(app)

    # Runing migrate
    db.init_app(app)
    bcrypt.init_app(app)
    migrate.init_app(app, db, compare_type = True)
    login_manager.init_app(app)

    from models import user, blacklist_token, product, cart, cart_items, order, order_detail

    from app import api_routes
    from app import web_routes

    return app
