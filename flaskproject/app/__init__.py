import os
from flask import Flask
from flask.ext.sqlalchemy import SQLAlchemy
from flask.ext.login import LoginManager
from flask.ext.bcrypt import Bcrypt


db = SQLAlchemy()
login_manager = LoginManager()
bcrypt = Bcrypt()


def create_app(config=None):
    app = Flask(__name__)
    app.config.from_object(config or os.environ.get('FLASK_CONFIG') or 'config')

    db.init_app(app)
    login_manager.init_app(app)
    from views import hello as hello_blueprint
    from auth import auth as auth_blueprint

    app.register_blueprint(hello_blueprint, url_prefix='/')
    app.register_blueprint(auth_blueprint, url_prefix='/auth')

    return app
