from flask import Flask
from flask.ext.sqlalchemy import SQLAlchemy
import datetime
import os

app = Flask(__name__)

# Attempt to load setting from a config file
app.config.from_envvar('HWSEA_SETTINGS', silent=True)

if 'SQLALCHEMY_DATABASE_URI' not in app.config or app.config['SQLALCHEMY_DATABASE_URI'] is None or len(app.config['SQLALCHEMY_DATABASE_URI']) == 0:
    if 'DB_NAME' not in app.config or app.config['DB_NAME'] is None or len(app.config['DB_NAME']) == 0:
        app.config['DB_NAME'] = '/tmp/test.db'
    app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///' + app.config['DB_NAME']
db = SQLAlchemy(app)


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
    zip_code = db.Column(db.String(10))  # includes - for 9 digit zip
    country = db.Column(db.String(2))
    created_on = db.Column(db.DateTime())

    def __init__(self, first_name, last_name,
                 address1, address2, city, state, zip_code):
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
        data = 'first: {0}, last: {1}, address1: {2}, address2: {3}, ' +\
               'city: {4}, state: {5}, zip: {6}, country: {7}, Date: {8}'
        return data.format(self.first_name,
                           self.last_name,
                           self.address1,
                           self.address2,
                           self.city,
                           self.state,
                           self.zip_code,
                           self.country,
                           self.created_on)


@app.before_request
def init_db():
    if not os.path.exists(app.config['DB_NAME']):
        db.create_all()


from app import views

if not views:
    print "We have a problem that we have no routes in views!!!"
