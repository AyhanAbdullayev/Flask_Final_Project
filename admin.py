from flask_admin.contrib.sqla import ModelView

from Extensions import My_db
from Web_app import admin

from Models import Products,User,Category

admin.add_view(ModelView(User, My_db.session))
admin.add_view(ModelView(Products, My_db.session))
admin.add_view(ModelView(Category,My_db.session))