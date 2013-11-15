# -*- coding: utf-8 -*-

from shared.database import Base

from sqlalchemy import Column, Integer, String, ForeignKey

class User(Base):
    ''''''
    __tablename__: 'users'
    id = Column(Integer, primary_key=True)
    name = Column(String)
    password = Column(String)
    def __init__(self, name=None, password=None):
        from hashlib import sha256
        from random import random
        self.name = name
        salt = sha256(str(random())).hexdigest()
        self.password = "sha256${salt}${hash}".format(salt=salt, hash=sha256(password + salt).hexdigest())
    def __repr__(self):
        return "<User(name='{0}', password='{1}')>".format(self.name, self.password)

class TX(Base):
    ''''''
    __tablename__: 'transactions'
    id = Column(Integer, primary_key=True)
    from_id = Column(String, ForeignKey('currencies.id'))
    to_id = Column(String, ForeignKey('currencies.id'))
    seller_id = Column(Integer, ForeignKey('users.id'))
    buyer_id = Column(Integer, ForeignKey('users.id'))
    def __init__(self, from_id=None, to_id=None, seller_id=None, buyer_id=None):
        self.from_id = from_id
        self.to_id = to_id
        self.seller_id = seller_id
        self.buyer_id = buyer_id
    def __repr__(self):
        return ""
