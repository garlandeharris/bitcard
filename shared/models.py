# -*- coding: utf-8 -*-

from time import time

from shared.database import Base

from sqlalchemy import Column, Integer, String, ForeignKey

class User(Base):
    ''''''
    __tablename__: 'users'
    
    id       = Column(Integer, primary_key=True)
    name     = Column(String)
    password = Column(String)
    
    def __init__(self, name=None, password=None):
        import bcrypt
        self.name     = name
        self.password = bcrypt.hashpw(password, bcrypt.gensalt())
    def __repr__(self):
        return "<User(name='{name}', password='{password}')>".format(name     = self.name,
                                                                     password = self.password)

class Currency(Base):
    ''''''
    __tablename__: 'currencies'

    id   = Column(String, primary_key=True)
    name = Column(String)
    url  = Column(String)

    def __init__(self, id=None, name=None, url=None):
        self.id   = id.upper()
        self.name = name
        self.url  = url
    def __repr__(self):
        return "<{id}(name='{name}', url='{url}'>".format(id   = self.id,
                                                          name = self.name,
                                                          url  = self.url)

class TX(Base):
    ''''''
    __tablename__: 'transactions'
    
    id        = Column(Integer, primary_key=True)
    amount    = Column(Integer)
    from_id   = Column(String,  ForeignKey('currencies.id'))
    to_id     = Column(String,  ForeignKey('currencies.id'))
    rate      = Column(Integer)
    seller_id = Column(Integer, ForeignKey('users.id'))
    buyer_id  = Column(Integer, ForeignKey('users.id'))
    timestamp = Column(Integer)
    
    def __init__(self, amount=None, from_id=None, to_id=None, rate=None, seller_id=None, buyer_id=None):
        self.amount    = amount
        self.from_id   = from_id
        self.to_id     = to_id
        self.rate      = rate
        self.seller_id = seller_id
        self.buyer_id  = buyer_id
        self.timestamp = int(time())
    def __repr__(self): # Idk if this is the best way to represent a TX
        return "<TX{id}({amount} {from}=>{to}, @{rate}, seller='{seller}', buyer='{buyer}') {timestamp}>".format(id        = self.id,
                                                                                                                 amount    = self.amount,
                                                                                                                 from      = self.from_id,
                                                                                                                 to        = self.to_id,
                                                                                                                 rate      = self.rate,
                                                                                                                 seller    = self.seller_id,
                                                                                                                 buyer     = self.buyer_id,
                                                                                                                 timestamp = self.timestamp)
