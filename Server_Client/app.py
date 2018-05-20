from flask import Flask,render_template
from models import Article
from exts import db

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'oracle://system:Woxhni.123@127.0.0.1/mydb'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = True
SQLALCHEMY_TRACK_MODIFICATIONS = False
db.init_app(app)

# db.create_all()
@app.route('/')
def index():
    return render_template('new_page.html')

if __name__ == '__main__':
    #最好关闭debug
    app.run()