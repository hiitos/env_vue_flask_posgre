from curses import echo
from sqlalchemy import create_engine, Column, Integer, String
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker
import subprocess
import os
from dotenv import load_dotenv
load_dotenv()

# from logging import getLogger
# logger = getLogger(__name__)

DATABASE = 'mysql+pymysql' # 'mysql+mysqlconnector'
USER = os.getenv('DB_USERNAME')
PASSWORD = os.getenv('DB_PASSWORD')
HOST = os.getenv('DB_HOST')
PORT = str(os.getenv('DB_PORT'))
DB_NAME = os.getenv('DB_DATABASE')

CONNECT_STR = '{}://{}:{}@{}:{}/{}'.format(DATABASE, USER, PASSWORD, HOST, PORT, DB_NAME)

# engineの設定 接続用のインスタンスを作成（create_engine関数がEngineインスタンスを返す）
engine = create_engine(CONNECT_STR,echo=True)

Base = declarative_base()
