# -*- coding: utf-8 -*-

from shared.conf import db

from sqlalchemy import create_engine
from sqlalchemy.orm import scoped_session, sessionmaker
from sqlalchemy.declarative import declarative_base

engine = create_engine("postgresql+psycopg2://{user}:{password}@{host}:{port}/{db_name}".format(
                            user=db['user'],
                            password=db['password'],
                            host=db['host'],
                            port=db['port'],
                            db_name=db['name']),
                        convert_unicode=True)
db_session = scoped_session(sessionmaker(autocommit=False,
                                         autoflush=False,
                                         bind=engine))
Base = declarative_base()
Base.query = db_session.query_property()

def init():
    import shared.models
    Base.metadata.create_all(bind=engine)
