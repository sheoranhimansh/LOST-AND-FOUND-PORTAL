from flask import *
from app import *
from app.user.models import *
from app.user.controllers import *
from app.found.models import *
from flask_sqlalchemy import *
from sqlalchemy import *
from flask import render_template,url_for,flash,jsonify,request

mod_found = Blueprint('found', __name__)

@mod_found.route('/found', methods=['GET'])
def found():
	user = User.query.filter(User.username==session['user_name']).first()
	#x = user.username
	#return x
	return render_template('found.html', user=user)
@mod_found.route('/addfound', methods=['POST'])
def addfound():
	#x=session['user_name']
	user = User.query.filter(User.username==session['user_name']).first()
	#x=user.username
	#return x
	category=request.form["CATEGORY"]
	brand=request.form["BRAND"]
	description=request.form["DESCRIPTION"]
	user_username=user.username
	status=request.form['STATUS']

	x=Found(category,brand,description,user_username,status)
	if x.category in ["WATCH","PEN","USB","BOOK","COMPUTER ACCESSORIES","KEYCHAIN","EARPHONES","OTHERS"]:
		try:
			db.session.add(x)
			db.session.commit()
			return render_template('dashboard.html',user=user)
		except:
			return make_response('ERROR :(',404,none)
	else:
		print('invalid category')
		return render_template('found.html',user=user)

@mod_found.route('/viewallfound',methods=['GET'])
def viewallfound():
	user = User.query.filter(User.username==session['user_name']).first()
	temp=Found.query.all()
	if len(temp)==0:
		return render_template('dashboard.html',user=user)
	else:		
		return render_template('k.html' ,user=user,found=temp)

@mod_found.route('/show', methods=['POST'])
def show():
	user = User.query.filter(User.username==session['user_name']).first()
	a=[]
	p=request.form.getlist('things')
	c=len(p)
	for i in range(c):
		tem = User.query.filter(User.username==p[i]).first()
		c={}
		c["name"]=tem.name
		c["email"]=tem.email
		c["mobile"]=tem.mobile
		a.append(c)
	if len(a)==0:
		return render_template('dashboard.html',user=user)
	else:
		return render_template('all.html',user=user,a=a)


	#x=Found.query.filter(Found.)


			


