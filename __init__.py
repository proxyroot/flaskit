from flask import Flask
from flask_admin import Admin
from configurations import DATABASE_URI

app = Flask(__name__)

admin = Admin(app, name='flaskit', template_mode='bootstrap3')

app.config['SQLALCHEMY_DATABASE_URI'] = DATABASE_URI
db = SQLAlchemy(app)

from flask_admin.contrib.sqla import ModelView
