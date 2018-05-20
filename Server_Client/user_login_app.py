from flask_sqlalchemy import SQLAlchemy
from flask import Flask, redirect, url_for, request
from flask_login import LoginManager, current_user, login_user, login_required
from login_model import User

app = Flask(__name__)
app.secret_key = 'Sqsdsffqrhgh.,/1#$%^&'
#app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///./db/blog.db'
app.config['SQLALCHEMY_DATABASE_URI'] = 'oracle://system:Woxhni.123@127.0.0.1/mydb'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = True
app.debug = True

db = SQLAlchemy(app)
login_manager = LoginManager()
login_manager.init_app(app)

password = '123'  # 只要用户输入的密码是 123 就可以登录


@login_manager.user_loader  # 使用user_loader装饰器的回调函数非常重要，他将决定 user 对象是否在登录状态
def user_loader(id):  # 这个id参数的值是在 login_user(user)中传入的 user 的 id 属性
    user = User.query.filter_by(id=id).first()
    return user


# 添加登录视图，如果是GET方法，返回一个简单的表单

@app.route('/login/', methods=['GET', 'POST'])
def login():
    if request.method == 'GET':
        return ''''' 
        <form action="#" method="POST"> 
    <span>请输入账号</span> 
    <input type="text" name="name" id="name" placeholder="name"> 
    <span>请输入密码</span> 
    <input type="password" name="pw" id="pw" placeholder="password"> 
    <input type="submit" name="submit"> 
       </form> 
        '''
    name = request.form.get('name')
    if request.form.get('pw') == password:
        user = User.query.filter_by(username=name).first()
        if not user:
            user = User(username=name)
            db.session.add(user)  # 如果没有 这个 用户 则创建
            db.session.commit()
        login_user(user)
        return redirect(url_for('index'))
    return 'Bad login'


# 如果密码是 123 就会跳转到视图函数 index 上

@app.route('/index/')
@login_required
def index():
    user = current_user
    return 'HelloWorld'


if __name__ == '__main__':
    app.run()

'''


load user 或者 session管理  
密码从db拿 
login required没起效 -->前端路由 不需要
怎么加入到现有的前端 ，ajax？-->留给 vue解决

'''