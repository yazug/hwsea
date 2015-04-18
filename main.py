#! /usr/bin/env python

from flask import Flask, render_template, request
from flask.ext.sqlalchemy import SQLAlchemy

import datetime
import os

app = Flask(__name__)
app.config['DB_NAME'] = '/tmp/test.db'
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///' + app.config['DB_NAME']
db = SQLAlchemy(app)

VERBOSE = True

class User(db.Model):
    ''' SQLAlchemy Record for User table '''
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
        self.created_on = datetime.datetime.now()

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


if not os.path.exists(app.config['DB_NAME']):
    db.create_all()


def validate_data(form_data):
    '''
        helper function for input verification
        used to make sure all required fields
        are present and reasonable
    '''
    valid = True
    for element in form_data.keys():
        if element != 'address2' and element != 'zip_code':
            if form_data[element] == '':
                if VERBOSE:
                    print 'bad ' + element
                valid = False
        elif element == 'zip_code':
            length = len(form_data[element])
            if length != 5 and length != 9:
                valid = False
    return valid


@app.route('/')
def welcome():
    ''' Welcome landing page '''
    return render_template('welcome.html')


@app.route('/newuser', methods=['GET', 'POST'])
def new_user():
    ''' Form and post endpoint for new user registration '''
    if request.method == 'POST':
        if VERBOSE:
            print request.form
        if validate_data(request.form) is True:
            new_record = User(
                request.form['first_name'],
                request.form['last_name'],
                request.form['address1'],
                request.form['address2'],
                request.form['city'],
                request.form['state'],
                request.form['zip_code'])
            if VERBOSE:
                print new_record
            db.session.add(new_record)
            db.session.commit()
            return render_template('thankyou.html')
        else:
            return render_template('validateerror.html')
    return render_template('newuser.html')


@app.route('/admin')
def list_users():
    ''' Admin page to list the users who have registered '''
    users = User.query.order_by(User.created_on)
    return render_template('admin.html', user_list=users)

if __name__ == "__main__":
    app.run(debug=True)
