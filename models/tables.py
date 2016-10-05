from sqlalchemy import Column, Integer, String
from . import db

class User(db.Model):
    __tablename__ = 'users'

    user_id = Column(Integer, primary_key=True)
    username = Column(db.String(60), nullable=False)
    email = Column(db.String(300), nullable=False)
    password = Column(db.String(32), nullable=False)

    def __init__(self, user_id=None username=None, email=None, password=None):
        self.user_id = user_id
        self.username = username
        self.email = email
        self.password = password

    def __repr__(self):
       return "<User(user_id='%r', username='%s', email='%s', password='%s')>" % (
                            self.user_id, self.username, self.email, self.password)
