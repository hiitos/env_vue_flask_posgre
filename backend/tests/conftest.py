import sys 
import os
sys.path.append(os.path.abspath(os.path.dirname(os.path.abspath(__file__)) + "/../src/"))

import pytest
from sqlalchemy.orm import sessionmaker
from model import Status
import sqlalchemy
from model import db
from model import Account

from model.db import engine
from model.db import Base
from model.Account import Account

@pytest.fixture(autouse=True)
def delete_account():
    Session = sessionmaker(bind=engine)
    ses = Session()
    ses.query(Account).delete()
    ses.commit()
    ses.close()
    yield 


