# -*- coding:utf-8 -*-
__author__ = 'shenj'

from sqlalchemy import create_engine
from sqlalchemy import Table, Column, Integer, String, MetaData, ForeignKey


database_url = 'mysql://root:shenjing@127.0.0.1:3306/test?charset=utf8'
engine = create_engine(database_url, echo=True)

metadata = MetaData()

users = Table('users', metadata,
              Column('id', Integer, primary_key=True),
              Column('name', String(40)),
              Column('fullname', String(40)),)

addresses = Table('addresses', metadata,
                  Column('id', Integer, primary_key=True),
                  Column('user_id', None, ForeignKey('users.id')),
                  Column('email_address', String(40), nullable=False),)

metadata.create_all(engine)

ins = users.insert().values(name='Jack', fullname='Jack Jones')
conn = engine.connect()
result = conn.execute(ins)



