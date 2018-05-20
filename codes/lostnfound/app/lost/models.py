from flask_sqlalchemy import *
from app import *
from app.user.models import *
from app.user.controllers import *
from app.found.models import *
from app.found.controllers import *


class Lost(db.Model):
	__tabelname__ = 'lost'
	id = db.Column(db.Integer,primary_key=True,autoincrement=True)
	category = db.Column(db.String(400))
	brand = db.Column(db.String(400))
	discription = db.Column(db.String(1000))
	user_username = db.Column(db.String(100),db.ForeignKey('login.username'))


	def __init__(self,category,brand,discription,user_username):
		self.category = category
		self.brand = brand
		self.discription = discription
		self.user_username = user_username


	def to_dict(self):
		return {
		'id' : self.id,
		'category' : self.category,
		'brand' : self.brand,
		'discription' : self.discription,
		'user_username' : self.user_username,
		}


	def __repr__(self):
		return "%r" % self.user_username
