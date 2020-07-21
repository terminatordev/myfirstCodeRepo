from flask import Flask
from flask_restful import Api
from flask_jwt import JWT
from security import authenticate, identity
from db import db
from resource.user import UserRegister
from resource.items import Item, Items
from resource.stores import Store,StoreList

app = Flask(__name__)
app.secret_key = 'dev'  # this is required to generate jwt access token,else /auth request will give error
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///mydata.db'
api = Api(app)


@app.before_first_request
def create_my_table():
    db.create_all()


jwt = JWT(app, authenticate, identity)

api.add_resource(StoreList,'/stores')
api.add_resource(Store,'/store/<string:name>')
api.add_resource(Items, '/items')
api.add_resource(Item, '/item/<string:name>')
api.add_resource(UserRegister, '/register')


# app.run(port=1234)
if __name__ == '__main__':
    db.init_app(app)
    app.run(port=1234, debug=True)  # in debug mode ,after code change no need to restart
