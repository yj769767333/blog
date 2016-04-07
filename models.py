# coding:utf-8

from datetime import datetime
from sqlalchemy import Column, Integer, String, DateTime, UnicodeText
from database import Base
from utils import md5

class User(Base):
    """用户表""" 
    __tablename__ = 'user'

    id = Column(Integer, primary_key=True)
    username = Column(String(64), unique=True, nullable=False)                # 登陆用户账号
    password = Column(String(64), nullable=True)                              # 密码
    create_time = Column(DateTime, nullable=False, default=datetime.now)      # 用户注册时间
    privilege = Column(Integer, default=1)                                    # 权重：1-普通用户 0-管理员
    
    def __init__(self, username=None, password=None):
        self.username = username
        self.set_password(password)

    def __repr__(self):
        return "<User %s>" % self.username

    def set_password(self, password):
        self.password = md5(password)

    def check_password(self, password):
        return self.password == md5(password)


class Post(Base):
    """文章表"""
    __tablename__ = 'post'

    id = Column(Integer, primary_key=True)
    title = Column(String(128), nullable=False)               # 标题
    content = Column(UnicodeText, nullable=False)             # 内容
    create_time = Column(DateTime, default=datetime.now)      # 创建时间
    update_time = Column(DateTime, default=datetime.now)      # 更新时间
    
    def __init__(self, title=None, content=None):
        self.title = title
        self.content = content

    def __repr__(self):
        return "<%s>" % self
