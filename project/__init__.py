from flask import Flask
from flask_sqlalchemy import SQLAlchemy

import warnings
from datetime import timedelta

warnings.filterwarnings("ignore", category=FutureWarning)
warnings.filterwarnings("ignore", category=DeprecationWarning)

app = Flask(__name__) # create the object of Flask class

app.secret_key= 'sessiondata'

app.secret_key='hrautomation@123' # secret key used for session

app.config['TESTING'] = True

app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = True

app.config['SQLALCHEMY_ECHO'] = True

app.config['SQLALCHEMY_RECORD_QUERIES'] = True

app.config['PERMANENT_SESSION_LIFETIME'] = timedelta(minutes=30)

app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql+pymysql://root:root@localhost:3306/pythondb' #pythondb  database which is already created in sqlyog

app.config['SQLALCHEMY_MAX_OVERFLOW'] = 0

db= SQLAlchemy(app)  # create the object of SQLAlchemy class

import project.com.controller