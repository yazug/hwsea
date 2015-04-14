#! /usr/bin/env python

from flask import Flask, render_template, request
from flask.ext.sqlalchemy import SQLAlchemy

import os

db_name = '/tmp/test.db'
app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///' + db_name
db = SQLAlchemy(app)

class User(db.Model):
    __tablename__ = 'tbl_users'
    user_id = db.Column(db.Integer, primary_key=True)
    first_name = db.Column(db.String(80))
    last_name = db.Column(db.String(80))
    address1 = db.Column(db.String(80))
    address2 = db.Column(db.String(80))
    city = db.Column(db.String(80))
    state = db.Column(db.String(2))
    zip_code = db.Column(db.String(9))
    country = db.Column(db.String(2))
    created_on = db.Column(db.DateTime())

    def __init__(self, first_name, last_name, address1, address2, city, state, zip_code):
        self.first_name = first_name
        self.last_name = last_name
        self.address1 = address1
        self.address2 = address2
        self.city = city
        self.state = state
        self.zip_code = zip_code
        self.country = 'US'

    def __repr__(self):
        data = 'first: {0}, last: {1}, address1: {2}, address2: {3}, city: {4}, state: {5}, zip: {6}, country: {7}, Date: {8}'
        return data.format(self.first_name,
                           self.last_name,
                           self.address1,
                           self.address2,
                           self.city,
                           self.state,
                           self.zip_code,
                           self.country,
                           self.created_on)

def validateData(formData):
    valid = True
    for element in formData.keys():
        if element != 'address2' and element != 'zip_code':
            if formData[element] == '':
                print 'bad ' + element
                valid = False
            else:
                print formData[element]
        elif element == 'zip_code':
            length = len(formData[element])
            print length
            if length != 5 or length != 9:
                print 'bad zip'
                valid = False
    return valid

@app.route('/')
def hello():
   return render_template('welcome.html', name='Jason')

@app.route('/newuser', methods=['GET', 'POST'])
def newUser():
    if request.method == 'POST':
        if validateData(request.form) is True:
            return '<html><body><h1>Thank You</h1></body></html>'
        else:
            return '<html><body><h1>Some Data is not valid!!!</h1></body></html>'
    return render_template('newuser.html')

@app.route('/admin/list')
def listUsers():
    results = ''
    users = User.query.order_by(User.created_on)
    return render_template('admin.html', user_list=users)

if __name__ == "__main__":
    if not os.path.exists(db_name):
        db.create_all()
    app.debug = True
    app.run()
