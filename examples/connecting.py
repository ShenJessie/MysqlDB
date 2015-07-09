# -*- coding:utf-8 -*-
__author__ = 'shenj'

import sqlalchemy
from sqlalchemy import create_engine

engine = create_engine("mysql://root:shenjing@127.0.0.1:3306/test?charset=utf8", echo=True)
