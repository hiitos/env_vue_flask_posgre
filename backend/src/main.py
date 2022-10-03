# render_template：参照するテンプレートを指定
# jsonify：json出力
from doctest import debug
from flask import Flask, render_template, jsonify
# CORS：Ajax通信するためのライブラリ
from flask_cors import CORS
# api.pyのファイル読み込み　（register_blueprintで使う）
# GET POSTとか書いてる
from api import api_bp
from random import *

# static_folder：vueでビルドした静的ファイルのパスを指定
# template_folder：vueでビルドしたindex.htmlのパスを指定
app = Flask(__name__, static_folder = "./../frontend/dist/static", template_folder="./../frontend/dist")

app.register_blueprint(api_bp)
app.config['JSON_AS_ASCII'] = False

CORS(app)

@app.route('/', defaults={'path': ''})
@app.route('/<path:path>')
# vueの画面にレンダリング
def index(path):
    return render_template('index.html')

# '/rand'が叩かれた時、乱数を生成
@app.route('/rand')
def random():
    response = {
        'randomNum': randint(1,4)
    }
    return jsonify(response)

# app.run(host, port)：hostとportを指定してflaskサーバを起動
if __name__ == '__main__':
    app.run(host='0.0.0.0', port=80,debug=True)
