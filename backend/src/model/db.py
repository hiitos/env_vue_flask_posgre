from sqlalchemy import create_engine, Column, Integer, String
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker
import subprocess

import config

DATABASE = 'mysql+pymysql' # 'mysql+mysqlconnector'
USER = config.DB_USERNAME
PASSWORD = config.DB_PASSWORD
HOST = config.DB_HOST
PORT = config.DB_PORT
DB_NAME = config.DB_DATABASE

CONNECT_STR = '{}://{}:{}@{}:{}/{}'.format(DATABASE, USER, PASSWORD, HOST, PORT, DB_NAME)

# engineの設定
engine = create_engine(CONNECT_STR)

Base = declarative_base()
