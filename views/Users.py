from flask_admin.contrib.sqla import ModelView
from . import admin, db
from models.tables import User

admin.add_view(ModelView(User, db.session))
