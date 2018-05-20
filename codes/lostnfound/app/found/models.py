from flask_sqlalchemy import *
from app import *
from app.user.models import *
from app.user.controllers import *


class Found(db.Model):
	__tabelname__ = 'found'
	id = db.Column(db.Integer,primary_key=True,autoincrement=True)
	category = db.Column(db.String(400))
	brand = db.Column(db.String(400))
	discription = db.Column(db.String(1000))
	user_username = db.Column(db.String(100),db.ForeignKey('login.username'))
	status = db.Column(db.String(1000))


	def __init__(self,category,brand,discription,user_username,status):
		self.category = category
		self.brand = brand
		self.discription = discription
		self.user_username = user_username
		self.status=status

	def to_dict(self):
		return {
		'id' : self.id,
		'category' : self.category,
		'brand' : self.brand,
		'discription' : self.discription,
		'user_username' : self.user_username,
		'status':self.status
		}


	def __repr__(self):
		return "%r" % self.user_username
