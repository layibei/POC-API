from flask import Flask, jsonify, abort, request, url_for, make_response , render_template
from flask_cors import CORS
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy import create_engine, MetaData

app = Flask(__name__)
app.config.from_object('config')


db = SQLAlchemy(app)
CORS (app)

engine = create_engine('oracle://system:Woxhni.123@127.0.0.1/mydb', convert_unicode=True)
metadata = MetaData(bind=engine)

class Customer(db.Model):
    __tablename__ = 's_customer'
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(80), unique=True)
    email = db.Column(db.String(320), unique=True)
    password = db.Column(db.String(32), nullable=False)




# list a particular task (GET method)
@app.route('/cust_detail/api/v1.0/get_by_id/<int:cust_id>', methods=['GET'])
def get_cust(cust_id):

    #cust_temp = Customer.query.filter_by(id=cust_id).first()
    #cust_all = Customer.query.all
    #cust_temp = Customer.query.filter_by(id=cust_id).first()

    #cust_temp = Customer.query.filter_by(id=cust_id)  # not work
    ## user engine to query db
    cust_temp=engine.execute('select * from s_customer where id = :id',id=cust_id).first()
    ## user model
    #r = Customer.select(Customer.c.id == 1).execute().first()
    #print(r)

    # if len(cust_temp)==0:
    #     abort(404)
    #     return make_response(jsonify({'error': 'Not found'}), 401)
    #     print('error')
    # else:
    cust_list = [cust for cust in cust_temp]
    print(cust_temp.name)

    #return jsonify({'cust': cust_list})  #list object
    return jsonify(
        [{'id': cust_temp.id,
          'name': cust_temp.name,
          'email': cust_temp.email,
          'password': cust_temp.password}])

    #if len(task_temp) == 0:
	# abort(404)

@app.route('/cust_detail/')
def static_page(name=None):
    return render_template('cust_detail.html', name=name)


if __name__ == '__main__':

    config = dict(
        debug=True,
        host='0.0.0.0',
        port=5000,
    )
    app.run(**config)