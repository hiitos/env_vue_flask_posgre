from flask import Blueprint, request, jsonify
from flask_restful import Api, Resource
# restAPI のフォルダのAccountApi.pyを読み込む
from restapi import AccountApi

system_account_id=999

api_bp = Blueprint('api', __name__, url_prefix='/api')

@api_bp.route('/account/get/<id>', methods=['GET'])
def getAccount(id):
    account_json = AccountApi.getById(id, system_account_id)
    return jsonify(account_json)

@api_bp.route('/account/create', methods=['POST'])
def createAccount():
    #payload = request.data.decode('utf-8')
    payload = request.json
    print(f"payload={payload}")
    response_json = AccountApi.create(payload, system_account_id)
    return jsonify(response_json)

@api_bp.route('/account/search', methods=['POST'])
def searchAccount():
    #payload = request.data.decode('utf-8')
    payload = request.json
    print(f"payload={payload}")
    response_json = AccountApi.search(payload, system_account_id)
    return jsonify(response_json)

@api_bp.route('/account/update', methods=['POST'])
def updateAccount():
    #payload = request.data.decode('utf-8')
    payload = request.json
    print(f"payload={payload}")
    response_json = AccountApi.update(payload, system_account_id)
    return jsonify(response_json)

@api_bp.route('/account/delete/<id>', methods=['GET'])
def deleteAccount(id):
    account_json = AccountApi.delete(id, system_account_id)
    return jsonify(account_json)

class Spam(Resource):
    def get(self):
        return {'id': 42, 'name': 'Name'}

api = Api(api_bp)
api.add_resource(Spam, '/spam')

