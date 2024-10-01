from flask import Flask
from flask_admin import Admin
Web_app = Flask(__name__)



Web_app.config["SQLALCHEMY_DATABASE_URI"] = "mysql://root:12345@localhost:3306/Flask_Back"
Web_app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = True
Web_app.config["FLASK_ADMIN_SWATCH"] = 'cerulean'
Web_app.config["SECRET_KEY"] = 'cc989c2e63787bd85f82cae17244c0ee345eb321'


admin = Admin(Web_app,name = "E-Shopper",template_mode = "bootstrap3")

from Controllers import *
from Extensions import *
from Models import *



if __name__ == "__main__":
    from admin import *
    Web_app.run(debug = True)