from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_login import LoginManager
from flask_wtf import FlaskForm,CSRFProtect
from flask_mail import Mail
from werkzeug.utils import secure_filename
from flask_restful import Api





app = Flask(__name__)
api=Api(app)

app.config['SECRET_KEY'] = '8ea2a86e42689205dde0ba81f31138b6'
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///road.db'

db = SQLAlchemy(app)

login_manager = LoginManager(app) 

app.config['MAIL_SERVER'] = 'smtp.gmail.com'
app.config['MAIL_PORT'] = 587
app.config['MAIL_USE_TLS'] = True
app.config['MAIL_USE_SSL'] = False
app.config['MAIL_USERNAME'] = 'emergenciaspace@gmail.com'
app.config['MAIL_PASSWORD'] = 'emergenciaspace@123'
app.config['MAIL_DEFAULT_SENDER'] = 'emergenciaspace@gmail.com'
mail = Mail(app)


from onroad import routes