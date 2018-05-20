from exts import db
from flask_login import UserMixin

''''' 
创建类的时候继承UserMixin ,有一些用户相关属性 

* is_authenticated ：是否被验证 
* is_active ： 是否被激活 
* is_anonymous : 是否是匿名用户 
* get_id() : 获得用户的id，并转换为 Unicode 类型 

'''


class User(db.Model, UserMixin):
    __tablename__ = 's_admins'
    id = db.Column(db.Integer, primary_key=True)
    #name = db.Column(db.String(50), unique=True)
    #login_count = db.Column(db.Integer, default=0)
    #last_login_ip = db.Column(db.String(128), default='unknown')
    username = db.Column(db.String(50), unique=True)
    email = db.Column(db.String(50), unique=True)
    password = db.Column(db.String(50), unique=True)
