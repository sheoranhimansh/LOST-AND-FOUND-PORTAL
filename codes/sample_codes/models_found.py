from flask_sqlalchemy import *
from app import *

#Class for found
class Found(db.Model):
	__tabelname__ = 'found'
	id = db.Column(db.Integer,primary_key=True,autoincrement=True)
	category = db.Column(db.String(400))
	brand = db.Column(db.String(400))
	discription = db.Column(db.String(1000))
	user_id = db.Column(db.Integer,db.ForeignKey('user.id'))


	def __init__(self,category,brand,discription,user_id):
		self.category = category
		self.brand = brand
		self.discription = discription
		self.user_id = user_id


	def to_dict(self):
		return {
		'id' : self.id,
		'category' : self.category,
		'brand' : self.brand,
		'discription' : self.discription,
		'user_id' : self.user_id,
		}


	def __repr__(self):
		return "%d" % self.id