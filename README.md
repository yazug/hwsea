# hwsea
A python based user registration and user list application using [Flask](http://flask.pocoo.org) and [SQLAlchemy](http://www.sqlalchemy.org)

User data is store in a [SQLite](http://www.sqlite.org) database in /tmp

## Setup
In order to run the project you need all of the python packages listed in requirements.txt
You can either install the packages in your global environment or by using a virtual environment.

### Global Setup
```sudo pip install -r requirements.txt```

### Python Virtual Environment (Recommended)
If you do not have the python virtual environment package perform the following:

```sudo pip install virtualenv```

Once installed setup a directory to store you virtual environments.

```mkdir virtualenvs```

Now create a virtual environment to run the application.

```virtualenv --no-site-packages hwsea```

Once the environment is setup it needs to be activated for your current shell.

```source /path/to/virtualenvs/hwsea/bin/activate```

Finally we need to add our packages, this is the same as the global setup only the packages are added to the virtual environment and not the system.

```pip install -r requirements.txt```

Now we are ready to run the application.

## Running the application
If you are using a virtual environment make sure to activate it.

```source /path/to/virtualenvs/hwsea/bin/activate```

Now, simply run main.py

```python main.py```

You will notice it will start a server on localhost (127.0.0.1) on port 5000. You can now use any web browser to use the application by using the following URL: http://127.0.0.1:5000

Once you are done using the application, the server can be stopped by hitting Ctrl-C.

If you are running a virtual environment, make sure to deactivate it.

``` deactivate ```
