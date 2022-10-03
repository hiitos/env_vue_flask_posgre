from model import db
from model import Account
from model import Status
from restapi import AccountApi
import json
import pprint
import datetime
import ujson
import requests
import pytest
from model.common import strftime
from model.common import strptime

def test_account_get():
    """
    restapi/getById
    """
    account = {
        'account_name' : 'flask_sv',
        'start_on' : '2021-05-05 00:00:00',
        'end_on' : '2030-12-31 00:00:00',
        'created_by' : 999,
        'created_at' : datetime.datetime.now(),
        'updated_by' : 999,
        'updated_at' : datetime.datetime.now(),
        'status' :  Status.getStatusKey("NEW")
    }

    Account.create(account, 999) == True

    account_dict = {
        'account_name' : "flask_sv",
        'end_on' : "2030-12-31 00:00:00"
    }
    result = Account.search(account_dict, 1)
    account_id = result[0].id

    # APIから確認
    url = f"http://localhost:5000/api/account/get/{account_id}"
    headers = {'Accept-Encoding': 'identity, deflate, compress, gzip',
               'Accept': '*/*', 'User-Agent': 'flask_sv/0.0.1',
               'Content-type': 'application/json; charset=utf-8',
               }
    response = requests.get(url, headers=headers)

    assert response.status_code == 200

    data = json.loads(response.text)
    assert data['body']['name'] == "account"
    assert data['body']['account_name'] == "flask_sv"
    assert data['body']['start_on'] == "2021-05-05 00:00:00"
    assert data['body']['end_on'] == "2030-12-31 00:00:00"
    assert data['status']['code'] == "I0001"
    assert data['status']['message'] == ""
    

def test_account_create():
    """
    """
    # modelから試験データ登録
    test_account_name = 'api_account_get'
    test_start_on = '2021-06-23 00:00:00'
    test_end_on = '2030-12-31 00:00:00'
    payload = {
        'account_name' : test_account_name,
        'start_on' : test_start_on,
        'end_on' : test_end_on
    }

    # createのテスト
    # APIの実行
    url = f"http://localhost:5000/api/account/create"
    headers = {'Accept-Encoding': 'identity, deflate, compress, gzip',
               'Accept': '*/*', 'User-Agent': 'flask_sv/0.0.1',
               'Content-type': 'application/json; charset=utf-8',
               }
    response = requests.post(url, headers=headers, json=payload)

    assert response.status_code == 200
    data = json.loads(response.text)
    assert data['body'] == ""
    assert data['status']['code'] == "I0001" 
    assert data['status']['message'] == "Created Account Succesfuly." 

    # 作成されたデータの確認
    account_dict = {
        'account_name' : test_account_name
    }
    result = Account.search(account_dict, 999)
    account_id = result[0].id

    result_json = AccountApi.getById(account_id, 100)

    assert result_json['body']['name'] == "account"
    assert result_json['body']['account_name'] == test_account_name
    assert result_json['body']['start_on'] == test_start_on
    assert result_json['body']['end_on'] == test_end_on
    assert result_json['status']['code'] == "I0001"
    assert result_json['status']['message'] == ""


def test_account_search():
    """
    """
    account = {
        'account_name' : "search_account",
        'start_on' : '2021-05-23 00:00:00',
        'end_on' : '2030-12-31 00:00:00',
        'created_by' : 999,
        'created_at' : datetime.datetime.now(),
        'updated_by' : 999,
        'updated_at' : datetime.datetime.now(),
        'status' :  Status.getStatusKey("NEW")
    }

    # createのテスト
    assert Account.create(account, 999) == True

    payload = {
        "account_name":"search_account",
        "start_on":"2021-05-23 00:00:00",
        "end_on":"2030-12-31 00:00:00"
    }
    #result = Account.search(query, 999)

    # APIから確認
    url = f"http://localhost:5000/api/account/search"
    headers = {'Accept-Encoding': 'identity, deflate, compress, gzip',
               'Accept': '*/*', 'User-Agent': 'flask_sv/0.0.1',
               'Content-type': 'application/json; charset=utf-8',
               }
    response = requests.post(url, headers=headers, json=payload)

    # HTTP Statusコードが200であること
    assert response.status_code == 200

    print(f"test_account_search():json response.text={response.text}")
    # BODYをjsonでパースできること
    data = json.loads(response.text)
    print(f"test_account_search():json data={data}")
    assert data['body'][0]['account_name'] == payload["account_name"]
    assert data['body'][0]['start_on'] == payload["start_on"]
    assert data['body'][0]['end_on'] == payload["end_on"]
    assert data['body'][0]['created_by'] == 999
    assert data['status']['code'] == 'I0001'
    assert data['status']['message'] == 'Found (1) records.'

def test_account_update():
    """
    """
    account = {
        'account_name' : "update_account",
        'start_on' : '2021-05-23 00:00:00',
        'end_on' : '2030-12-31 00:00:00',
        'created_by' : 999,
        'created_at' : datetime.datetime.now(),
        'updated_by' : 999,
        'updated_at' : datetime.datetime.now(),
        'status' :  Status.getStatusKey("NEW")
    }

    # create
    Account.create(account, 999) == True

    search_query = {
        "account_name":"update_account",
        "start_on":"2021-05-23 00:00:00",
        "end_on":"2030-12-31 00:00:00"
    }
    result = Account.search(search_query, 999)
    assert result[0].account_name == account['account_name']
    account_id = result[0].id
    payload = {
        "id": account_id,
        "account_name":"update_account_modified",
        "start_on":"2021-05-24 10:00:00",
        "end_on":"2030-12-31 12:00:00",
        "status":"2"
    }

    # APIから確認
    url = f"http://localhost:5000/api/account/update"
    headers = {'Accept-Encoding': 'identity, deflate, compress, gzip',
               'Accept': '*/*', 'User-Agent': 'flask_sv/0.0.1',
               'Content-type': 'application/json; charset=utf-8',
               }
    response = requests.post(url, headers=headers, json=payload)

    # HTTP Statusコードが200であること
    assert response.status_code == 200
    data = json.loads(response.text)
    assert data['body'] == ""
    assert data['status']['code'] == "I0001"
    assert data['status']['message'] == "Updated Account Succesfuly."

    search_query = {
        "account_name":"update_account_modified",
    }
    result = Account.search(search_query, 999)
    assert result[0].start_on.strftime('%Y-%m-%d %H:%M:%S') == payload['start_on'] #.strftime('%Y–%m–%d %H:%M:%S')
    assert result[0].end_on.strftime('%Y-%m-%d %H:%M:%S') == payload['end_on'] #.strftime('%Y–%m–%d %H:%M:%S')
    assert result[0].created_by == 999
    assert result[0].status == 2


def test_account_delete():
    """
    """
    account = {
        'account_name' : "delete_account",
        'start_on' : '2021-05-23 00:00:00',
        'end_on' : '2030-12-31 00:00:00',
        'created_by' : 999,
        'created_at' : datetime.datetime.now(),
        'updated_by' : 999,
        'updated_at' : datetime.datetime.now(),
        'status' :  Status.getStatusKey("NEW")
    }

    # create
    Account.create(account, 999) == True

    search_query = {
        "account_name":"delete_account",
        "start_on":"2021-05-23 00:00:00",
        "end_on":"2030-12-31 00:00:00"
    }
    result = Account.search(search_query, 999)
    assert result[0].account_name == account['account_name']
    account_id = result[0].id

    # APIから確認
    url = f"http://localhost:5000/api/account/delete/{account_id}"
    headers = {'Accept-Encoding': 'identity, deflate, compress, gzip',
               'Accept': '*/*', 'User-Agent': 'flask_sv/0.0.1',
               'Content-type': 'application/json; charset=utf-8',
               }
    response = requests.get(url, headers=headers)

    # HTTP Statusコードが200であること
    assert response.status_code == 200

    data = json.loads(response.text)
    print(f"test_AccountApi#test_account_delete data={data} code={data['status']['code']} message={data['status']['message']}")
    assert data['body'] == ""
    assert data['status']['code'] == "I0001"
    assert data['status']['message'] == "deleted Account Succesfuly."

    
