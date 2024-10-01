from Web_app import Web_app
from flask_migrate import Migrate
from flask_sqlalchemy import SQLAlchemy
from flask_wtf.csrf import CSRFProtect
from flask_login import LoginManager



My_db = SQLAlchemy(Web_app)

migrate = Migrate(Web_app,My_db)

CSRF = CSRFProtect(Web_app)

login_manager = LoginManager(Web_app)

login_manager.login_view = "Login_Page"