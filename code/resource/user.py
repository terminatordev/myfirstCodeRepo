import sqlite3
from flask_restful import Resource,reqparse
from model.user import UserModel

class UserRegister(Resource):
    parser=reqparse.RequestParser()

    parser.add_argument('username',
                        type=str,
                        required=True,
                        help="Username cannot be blank")
    parser.add_argument('password',
                        type=str,
                        required=True,
                        help="password cannot be blank")

    def post(self):
        reqdata=UserRegister.parser.parse_args()
        existinguser=UserModel.find_by_username(reqdata['username'])
        print("reqdata is: ",reqdata)
        if existinguser:
            return ({'message':'user already exists'},400)

        newuser=UserModel(reqdata['username'],reqdata['password'])
        newuser.save_to_db()
        return ({'message':'user registered successfully'},201)
