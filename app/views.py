from app import app
from app import db
from app import User

from flask import render_template, request

VERBOSE = True


def validate_form_data(form_data):
    '''
        helper function for input verification
        used to make sure all required fields
        are present and reasonable
    '''
    valid = True
    keys = form_data.keys()
    keys_to_check = [
        'first_name',
        'last_name',
        'address1',
        'address2',
        'city',
        'state',
        'zip_code',
        'country'
    ]

    # Check for enough of the keys that we care about
    for col in keys_to_check:
        if col not in keys:
            valid = False

    if valid:
        for element in keys:
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
        if validate_form_data(request.form) is True:
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
