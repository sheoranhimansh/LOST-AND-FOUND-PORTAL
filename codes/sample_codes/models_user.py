from flask import *
from flask_sqlalchemy import *
from app import *
from werkzeug.security import generate_password_hash, check_password_hash

app=Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:////tmp/test.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = True
db=SQLAlchemy(app)
db.create_all()

#User class
class User(db.Model):
	__tabelname__ = 'users'
	id=db.Column(db.Integer,primary_key=True,autoincrement=True)
	name = db.Column(db.String(255))
	email = db.Column(db.String(255), unique=True)
	password = db.Column(db.String(255))
	mobile_no = db.Column(db.Integer, unique=True)
	#lost = db.relationship('Lost' , backref='userlost' , lazy='dynamic')
	#found = db.relationship('Found' , backref='userfound' , lazy='dynamic')

	def __init__(self,name,email,password,mobile_no):
		self.name = name
		self.email = email
		self.password = generate_password_hash(password)
		self.mobile_no = mobile_no


	def check_password(self,password):
		return check_password_hash(self.password, password)


	def to_dict(self):
		return {
		'id' : self.id,
		'name' : self.name,
		'email' : self.email,
		'mobile_no' : self.mobile_no,
		}


	def __repr__(self):
		return "%d" % self.id




