from flask import *
from app import *
from app.user.models import *
from app.user.controllers import *
from app.found.models import *
from app.lost.models import *
from app.lost.controllers import *
from flask_sqlalchemy import *
from sqlalchemy import *
from sqlalchemy import and_
from flask import render_template,url_for,flash,jsonify,request
from app.new.models import *
from sqlalchemy import exists

mod_lost = Blueprint('lost', __name__)

@mod_found.route('/lost', methods=['GET'])
def lost():
	user = User.query.filter(User.username==session['user_name']).first()
	#x = user.username
	#return x
	return render_template('lost.html', user=user)

@mod_found.route('/addlost', methods=['POST'])
def addlost():
	#x=session['user_name']
	user = User.query.filter(User.username==session['user_name']).first()
	#x=user.username
	#return x
	category=request.form["CATEGORY"]
	brand=request.form["BRAND"]
	description=request.form["DESCRIPTION"]
	user_username=user.username
	listlost = Found.query.filter(Found.category==category).all()
	x=Lost(category,brand,description,user_username)
	if x.category in ["WATCH","PEN","USB","BOOK","COMPUTER ACCESSORIES","KEYCHAIN","EARPHONES","OTHERS"]:
		try:
			db.session.add(x)
			db.session.commit()
			return render_template('dashboard.html',user=user)
		except:
			return make_response('ERROR :(',404,none)
	print('invalid category')
	return render_template('lost.html',user=user)

@mod_found.route('/search', methods=['POST','GET'])
def hush():
	
	user = User.query.filter(User.username==session['user_name']).first()

	temp=Lost.query.filter(user.username==Lost.user_username).all()
	if temp==0:
		return render_template('dashboard.html',user=user)
	else:
	#return render_template('p.html',user=user,record=temp)
		a=[]
		length=0
		for i in temp:
			print(i.category+i.brand)
			record=Found.query.filter(and_(i.category==Found.category , i.brand==Found.brand)).all()
		#return jsonify(record.user_username)
		#return render_template('p.html',user=user,record=record)
			for j in record:
				rest=User.query.filter(User.username==j.user_username).first()
		#return jsonify(rest.username)
				c={}
				c["username"]=rest.username
				c["email"]=rest.email
				c["mobile"]=rest.mobile
				c["category"]=j.category
				c["brand"]=j.brand
				c["lostid"]=i.id
				c['foundid']=j.id
				c["status"]=j.status
				c['mix']=str(i.id)+','+str(j.id)+','+rest.username+','+j.status
				length+=1
				a.append(c)
		if length==0:
			return render_template('dashboard.html',user=user)
		else:
			return render_template('hush.html',user=user,a=a)	

@mod_found.route('/relation', methods=['POST','GET'])
def relatio():
	user = User.query.filter(User.username==session['user_name']).first()
	h=request.form.getlist('thin')
	for j in h:
		k=j.split(",")
		appl= Found.query.filter(Found.id==k[1]).first()
		if appl.status=="RESOLVED":
			c=NEW.query.filter(NEW.item==k[1]).first()
			#x=User.query.filter(User.username==i.name1).first()
			z=NEW(c.name2,user.username,appl.id,c.name2)
			db.session.add(z)
			db.session.commit()
			db.session.delete(c)
			db.session.commit()
		else:
			appl.status="RESOLVED"
			db.session.commit()
			te = User.query.filter(User.username==k[2]).first()
			s=NEW(user.username,te.username,appl.id,user.username)
			db.session.add(s)
			db.session.commit()
		if len(h)>0:
			return render_template('dashboard.html',user=user)




	a=[]
	z=request.form.getlist('thins')
	#return jsonify(len(z))
	if len(z)>0:
		w=z.split(",")
		print(w) 
		apple= Found.query.filter(Found.id==w[1]).first()
		tem = User.query.filter(User.username==w[2]).first()
		if apple.status=='ACTIVE' or apple.status=='CLAIM':
			apple.status='CLAIM'
			db.session.commit()
			
			return render_template("dashboard.html",user=user)


		elif apple.status=='RESOLVED':
			c={}
			c["name1"]=user.name
			c["mobile1"]=user.mobile
			c["name2"]=tem.name
			c["mobile2"]=tem.mobile
			c["category"]=apple.category
			c["brand"]=apple.brand
			c["discription"]=apple.discription
			a.append(c)
			return render_template("rela.html",user=user,a=a)


	#h=request.form.getlist('thin')
	#for j in range(len(h)):

		#	q=NEW(user.name,user.mobile,tem.name,tem.mobile,apple.category,apple.brand,apple.discription)
		#	db.session.add(q)
		#	db.session.commit()
		
	#h=request.form.getlist('thin')
	#for i in range(len(h))




@mod_found.route('/fast', methods=['POST','GET'])
def fas():
	user = User.query.filter(User.username==session['user_name']).first()
	b=NEW.query.all()
	a=[]
	for i in b:
		x=User.query.filter(User.username==i.name1).first()
		y=User.query.filter(User.username==i.name2).first()
		z=Found.query.filter(Found.id==i.item).first()
		f=User.query.filter(User.username==i.owner).first()
		c={}
		c["name1"]=x.name
		c["mobile1"]=x.mobile
		c["name2"]=f.name
		c["mobile2"]=f.mobile
		c["category"]=z.category
		c["brand"]=z.brand
		c["discription"]=z.discription
		a.append(c)
	return render_template("rela.html",user=user,a=a)



@mod_found.route('/debug', methods=['GET','POST'])
def dela():
	c=request.form["yolo"]
	p=Lost.query.filter(Lost.id==c).first()
	db.session.delete(p)
	db.session.commit()
	user = User.query.filter(User.username==session['user_name']).first()

	tem = Lost.query.filter(Lost.user_username==user.username).all()
	
	return render_template('dashboard.html',user=user,tem=tem)

@mod_found.route('/debu', methods=['GET','POST'])
def de():
	c=request.form["yolo"]
	p=Found.query.filter(Found.id==c).first()
	db.session.delete(p)
	db.session.commit()
	user = User.query.filter(User.username==session['user_name']).first()

	tem = Found.query.filter(Found.user_username==user.username).all()
	
	return render_template('dashboard.html',user=user,tem=tem)



@mod_lost.route('/ilost', methods=['POST','GET'])
def f():
	user = User.query.filter(User.username==session['user_name']).first()

	tem = Lost.query.filter(Lost.user_username==user.username).all()
	if len(tem)==0:
		return render_template('dashboard.html',user=user)
	else:
		return render_template('haha.html',user=user,tem=tem)



@mod_found.route('/ifound', methods=['POST','GET'])
def s():
	user = User.query.filter(User.username==session['user_name']).first()
	tem = Found.query.filter(Found.user_username==user.username).all()
	if len(tem)==0:
		return render_template('dashboard.html',user=user)
	else:
		return render_template('haha.html',user=user,tem=tem)

	
	
