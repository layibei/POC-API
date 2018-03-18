from flask import Flask
from flask_sqlalchemy import SQLAlchemy
"""
import db

class Cmms(db.Model):
    __tablename__ = 'c_cmms'
    item_id = db.Column(db.Integer, primary_key=True)
    item_name = db.Column(db.String(20), unique=True)
    option_id = db.Column(db.Integer, unique=True)
    option_value = db.Column(db.String(40), nullable=False)

    def get_country_list(country_list):

        #country_list = engine.execute('select * from c_cmms where item_name = :id', id='country').first()
        country_list = Cmms.query.filter(Cmms.item_name == "country").all()
        print(country_list)
        return country_list
"""