import sqlite3
from db import db
class UserModel(db.Model):

    __tablename__="users"
    id=db.Column(db.Integer,primary_key=True)
    name=db.Column(db.String(80))
    password=db.Column(db.String(80))

    def __init__(self,name,pwd):
        # self.id=_id
        self.name=name
        self.password=pwd

    @classmethod
    def find_by_username(cls,uname):
        out_user=cls.query.filter_by(name=uname).first()
        return out_user

    @classmethod
    def find_by_userid(cls,_id):
        out_user=cls.query.filter_by(id=_id).first()
        return out_user

    def save_to_db(self):
        db.session.add(self)
        db.session.commit()
