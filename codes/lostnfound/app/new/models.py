from flask_sqlalchemy import *
from app import *
from app.user.models import *
from app.user.controllers import *
from app.lost.models import *
from app.found.models import *
from app.lost.controllers import *
from app.found.controllers import *



class NEW(db.Model):
	__tabelname__ = 'NEW'
	id = db.Column(db.Integer,primary_key=True,autoincrement=True)
	name1=db.Column(db.String(40),db.ForeignKey('login.username'))
	name2=db.Column(db.String(40),db.ForeignKey('login.username'))
	item=db.Column(db.Integer,db.ForeignKey('found.id'))
	owner=db.Column(db.String(312),db.ForeignKey('login.username'))


	def __init__(self,name2,name1,item,owner):
		self.name1 = name1
		self.name2 = name2
		self.item = item
		self.owner = owner

	def to_dict(self):
		return {
		'name1':self.name1,
		'name2':self.name2,
		'item':self.item,
		'owner':self.owner,
		}

	def __repr__(self):
		return "%d" % self.item