import pymysql
import sqlalchemy

pymysql.install_as_MySQLdb()
from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()
engine = create_engine("mysql://root:1234@localhost/qq_bot_hdu?charset=utf8")


class qq_bot_hdu(Base):
    __tablename__ = "qq_bot_hdu"

    qq = sqlalchemy.Column(sqlalchemy.String(12), primary_key=True)
    user_name = sqlalchemy.Column(sqlalchemy.Integer)
    password = sqlalchemy.Column(sqlalchemy.String(31))
    token = sqlalchemy.Column(sqlalchemy.String(255))
    CASTGC = sqlalchemy.Column(sqlalchemy.String(255))
    tp_up = sqlalchemy.Column(sqlalchemy.String(255))
    time = sqlalchemy.Column(sqlalchemy.DateTime)

    def __init__(self, qq, user_name, password, token, CASTGC, tp_up, time):
        self.qq = qq
        self.user_name = user_name
        self.password = password
        self.token = token
        self.CASTGC = CASTGC
        self.tp_up = tp_up
        self.time = time


class jiaowuchu(Base):
    __tablename__ = "jiaowuchu"

    url = sqlalchemy.Column(sqlalchemy.String(255), primary_key=True)
    title = sqlalchemy.Column(sqlalchemy.String(255))
    send_flag = sqlalchemy.Column(sqlalchemy.Integer)
    time = sqlalchemy.Column(sqlalchemy.DateTime)

    def __init__(self, url, title, send_flag, time):
        self.url = url
        self.title = title
        self.send_flag = send_flag
        self.time = time


class jiaowuchu_user(Base):
    __tablename__ = "jiaowuchu_user"

    user_id = sqlalchemy.Column(sqlalchemy.String(255), primary_key=True)
    user_type = sqlalchemy.Column(sqlalchemy.String(255))

    def __init__(self, user_id, user_type):
        self.user_id = user_id
        self.user_type = user_type


class fanya_user(Base):
    __tablename__ = "fanya"

    qqid = sqlalchemy.Column(sqlalchemy.String(255), primary_key=True)
    username = sqlalchemy.Column(sqlalchemy.String(255), primary_key=True)
    password = sqlalchemy.Column(sqlalchemy.String(255), primary_key=True)

    def __init__(self, qqid, username, password):
        self.qqid = qqid
        self.username = username
        self.password = password


def db_session():
    DbSession = sessionmaker(bind=engine)
    return DbSession()
