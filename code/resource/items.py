from flask_jwt import jwt_required
from flask_restful import Resource,reqparse
from model.items import ItemModel
import sqlite3


class Items(Resource):
    #@jwt_required()
    def get(self):
        
        return {'items':[it.json() for it in ItemModel.query.all()]}

class Item(Resource):
    parser=reqparse.RequestParser()

    parser.add_argument('price',
                        type=float,
                        required=True,
                        help='This field can not be blank')
    parser.add_argument('storeid',
                        type=int,
                        required=True,
                        help='Give store id for each item')

    @jwt_required()
    def get(self,name):
        it=ItemModel.find_item_by_name(name)
        print("get item ,value of item",it)
        if it:
            return it.json(),200

        return {'message':'Item not found'},400

    def post(self,name):
        # reqdata=request.get_json()
        item=ItemModel.find_item_by_name(name)
        if item:
            return({'message':'Item with that name already exists'},400)

        reqdata=Item.parser.parse_args()
        new_item=ItemModel(name,reqdata['price'],reqdata['storeid'])
        try:
            new_item.save_to_db()
        except:
            return ({"message":"Error while inserting to database"},500)

        return new_item.json(),201

    def delete(self,name):
        item=ItemModel.find_item_by_name(name)
        if item:
            item.delete_from_db()
            return {'message':'item deleted'}
        return({'message':'Item Not Found'},400)

    def put(self,name):
        reqdata=Item.parser.parse_args()
        # print("User given args are: ",reqdata)
        # reqdata=request.get_json()
        fetch_item=ItemModel.find_item_by_name(name)

        print("fetched item in put method: ",fetch_item)
        if fetch_item:
            # get_item=itemobj.get(fetch_item['name'])
            fetch_item.price=reqdata['price']
            fetch_item.store_id=reqdata['storeid']
            try:
                fetch_item.save_to_db()
                return ({'message':'item updated'},200)
            except:
                return ({"message":"Error while updating item to database"},500)
        else:
            new_item=ItemModel(name,reqdata['price'],reqdata['storeid'])
            try:
                new_item.save_to_db()
                return ({'message':'item Inserted'},200)
            except:
                return ({"message":"Error while inserting item to database"},500)
            return new_item.json()
