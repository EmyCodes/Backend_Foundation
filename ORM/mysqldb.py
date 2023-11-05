#!/usr/bin/python3

from sqlalchemy import create_engine
from database_info import username, passwd

engine = create_engine(f'mysql+mysqldb://{username}:{passwd}@localhost/Emy')
engine.connect()
print(engine)
