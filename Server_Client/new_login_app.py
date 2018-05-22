#!/usr/bin/env python
# encoding: utf-8
## 匿名login
from flask import Flask, Blueprint, session,request,render_template
from flask_login import LoginManager, current_user, login_user, logout_user, login_required, UserMixin
from exts import db
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'oracle://system:Woxhni.123@127.0.0.1/mydb'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = True
app.debug = True


# user models
class User(db.Model, UserMixin):
    __tablename__ = 's_admins'
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(50), unique=True)
    email = db.Column(db.String(50), unique=True)
    password = db.Column(db.String(50), unique=True)

    def is_authenticated(self):
        return True

    def is_actice(self):
        return True

    def is_anonymous(self):
        return False

    def get_id(self):
        return "1"


app.secret_key = 's3cr3t'
db = SQLAlchemy(app)
login_manager = LoginManager()
login_manager.session_protection = 'strong'
login_manager.login_view = 'auth.login'
login_manager.init_app(app)


@login_manager.user_loader
def load_user(user_id):
    user = User.query.filter_by(id=user_id).first()
    return user


# url redirect
auth = Blueprint('auth', __name__)


@auth.route('/login', methods=['GET', 'POST'])
def login():
    print("$$$$", current_user)
    print(any(current_user.__dict__))
    if any(current_user.__dict__):
        if current_user.id == 1:
            msg = "login already"
            pass
    else:
        name = 'jen' ## have to make a form for input the username and pwd
        user = User.query.filter_by(username=name).first()
        session['site'] = 'AMH' ##init session info
        print(session['site'])
        login_user(user)
        msg = "login successfully"
        print(msg)
    print("aaaaa",current_user.__dict__)
    print("bbbbb", session['site'])

    return "login page: %s" % msg


@auth.route('/login2', methods=['GET', 'POST'])
def signin():
    if request.method == 'GET':
        return render_template("login.html")
    if request.method == 'POST':
        u = request.form.get('name')
        p = request.form.get('pw')
        ''' can refer to this
        if isNameExisted(u):
            t = checkPassword(u);#获得数据库存储的hash值
            if check_password_hash(t,p):#查询有没有这个用户
                session['logged_in'] = True # 登录成功
                return redirect('/user/blog')
        else:#没有用户就是新用户那么就转入注册页面
            return redirect('/register')
        '''
        user = User.query.filter_by(username=u).first()
        if p == user.password:
            login_user(user)
            msg = "login successfully"
        else:
            msg = "passwd is wrong"
    return "login page: %s" % msg




@auth.route('/logout', methods=['GET', 'POST'])
def logout():
    logout_user()
    return "logout page"


# test method
@app.route('/test')
@login_required
def test():
    u = session['user_id']  # handle when return none
    print(u)
    # return "yes , you are allowed"
    return 'User %s have login' % u


app.register_blueprint(auth, url_prefix='/auth')
app.run(debug=True)

'''
login page
1 判断session是否login
    是：返回msg： xxx已经login
    否：提供form：填写login信息，提交。
        提交验证成功： 返回msg
        不成功： 返回msg

logout 页面 @login required
1 提供logout按钮，
    点logout：更新session，登出。 返回 msg。

选site页面 @login required
1 提供 form 填写 site 信息。提交。
    成功：更新session（site info），返回msg
    失败：返回msg
'''