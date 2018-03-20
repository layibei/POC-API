from flask import Flask, jsonify, abort, request, url_for, make_response , render_template,json
from flask_cors import CORS
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy import create_engine, MetaData
#from model.cmms import Cmms

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

    def get_all(c_list):
        cust_temp = Customer.query.all()
        print(cust_temp)
        #obj_arr = []

        for cu_item in cust_temp:
            a = cu_item.__dict__
            print(a)
            a.pop('_sa_instance_state', None)
            dict = {}
            dict.update(a)
            c_list.append(dict)

        print(c_list)
        return c_list


class Cmms(db.Model):
    __tablename__ = 'c_cmms'
    key = db.Column(db.Integer, primary_key=True)
    item_id = db.Column(db.Integer, unique=False)
    item_name = db.Column(db.String(20), unique=False)
    option_id = db.Column(db.Integer, unique=False)
    option_value = db.Column(db.String(40), nullable=False)

    def get_country_list(country_list):
        #country_temp = engine.execute('select * from c_cmms where item_name = :id', id='country')
        country_temp = Cmms.query.filter(Cmms.item_id == "1").all()
        #country_temp = Cmms.query.all()
        # print('country_list:')
        # print(len(country_temp))
        print(len(country_temp))
        for country_item in country_temp:
             a = country_item.__dict__
             print(a)
             a.pop('_sa_instance_state', None)
             dict = {}
             dict.update(a)
             country_list.append(dict)

        print('country_list')
        print(country_list)

        return country_list


# list a particular task (GET method)
#@app.route('/cust_detail/api/v1.0/get_all', methods=['GET'])
@app.route('/api/v1.0/get_cust_detail/', methods=['GET'])
def get_cust():

    #cust_temp=engine.execute('select * from s_customer where 1=1').first()
    # cust_temp = Customer.query.all()
    #
    # obj_arr = []
    #
    # for cu_item in cust_temp:
    #     a = cu_item.__dict__
    #     print(a)
    #     a.pop('_sa_instance_state', None)
    #     dict = {}
    #     dict.update(a)
    #     obj_arr.append(dict)
    #
    # print(obj_arr)  --> move to Customer.get_all()
    c_list = []
    Customer.get_all(c_list)

    return jsonify({'customer': c_list})

@app.route('/api/v1.0/get_cust_detail/<int:cust_id>', methods=['GET'])
def get_cust_id(cust_id):
    cust_temp = engine.execute('select * from s_customer where id = :id', id=cust_id).first()

    c_list = [{'id': cust_temp.id, 'name': cust_temp.name, 'email': cust_temp.email, 'password': cust_temp.password}]
    #return jsonify(
    #    [{'id': cust_temp.id, 'name': cust_temp.name, 'email': cust_temp.email, 'password': cust_temp.password}])
    return jsonify({'customer': c_list})


@app.route('/cust_all/')
def cust_all(name=None):
    return render_template('cust_all.html', name=name)

@app.route('/cust_detail/')
def cust_detail(name=None):

    return render_template('cust_detail.html', name=name)

@app.route('/api/v1.0/get_static_data/', methods=['GET'])
def get_static():
    country_list = []
    Cmms.get_country_list(country_list)

    return jsonify({'country': country_list})

@app.route('/api/v1.0/get_cust_detail/<int:cust_id>', methods=['PUT'])
def update_cust(cust_id):
    #cust_temp = engine.execute('select * from s_customer where id = :id', id=cust_id).first()

    # cust_temp.id = request.json.get('id', cust_temp.id)
    # cust_temp.name = request.json.get('name', cust_temp.name)
    # cust_temp.email = request.json.get('email', cust_temp.email)
    print("*************")
    print(request.json)
    c_list=[]
    #c_list = [{ 'id': cust_temp.id , 'name' : cust_temp.name , 'email' : cust_temp.email }]
    return jsonify({'customer': c_list })


if __name__ == '__main__':

    config = dict(
        debug=True,
        host='0.0.0.0',
        port=5000,
    )
    app.run(**config)