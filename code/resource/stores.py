from flask_restful import Resource
from model.stores import StoreModel

class Store(Resource):
    def get(self,name):
        store=StoreModel.find_store_by_name(name)
        if store:
            return store.json()
        return {'message':'Store not found'},404

    def post(self,name):
        store=StoreModel.find_store_by_name(name)
        if store:
            return {'message':'Store with that name already exists'},400
        new_store=StoreModel(name)
        try:
            new_store.save_to_db()
        except:
            return {'message':'Error while creating a store'},500
        return new_store.json(), 201

    def delete(self,name):
        store=StoreModel.find_store_by_name(name)
        if store:
            try:
                store.delete_from_db()
            except:
                return {'message':'Error in deleting store'},500
            return {'message':'Store deleted successfully'}
        return {'message':'Store not there to delete'}


class StoreList(Resource):
    def get(self):
        return {'stores':[store.json() for store in StoreModel.query.all()]}
