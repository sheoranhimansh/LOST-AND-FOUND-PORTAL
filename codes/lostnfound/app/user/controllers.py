from flask import *
from sqlalchemy.exc import IntegrityError
from app import db
from app.user.models import User

mod_user = Blueprint('user', __name__)

@mod_user.route('/addUser',methods=['POST'])
def add_user():
	print('started')
	first_name = request.form["first_name"]
	last_name = request.form["last_name"]
	password = request.form["password"]
	username = request.form["username"]
	gender = request.form["gender"]
	country = request.form["country"]
	mobile= request.form["mobile"]
	email = request.form["email"]
	date = request.form["date"]
	month = request.form["month"]
	year = request.form["year"]
	print(username, first_name, last_name, email, mobile, month, date, year, country, gender, password)
	user=User(username,first_name,last_name,email,mobile,month,date,year,country,gender,password)
	print('reached')
	db.session.add(user)
	db.session.commit()
	return "You have signed in successfully"


@mod_user.route('/', methods=['GET'])
def home():
	if 'user_name' in session:
		return redirect('/dashboard')
	return render_template('homepage.html')


@mod_user.route('/homepage', methods=['GET'])
def homepage():
	if 'user_name' in session:
		return redirect('/dashboard')
	return render_template('homepage.html')

@mod_user.route('/dash', methods=['GET'])
def dash():
	return redirect('/dashboard')

@mod_user.route('/dashboard', methods=['GET'])
def dashboard():
	user = User.query.filter(User.username==session['user_name']).first()
	return render_template('dashboard.html',user=user)

@mod_user.route('/reset', methods=['GET'])
def reset():
	return render_template('reset.html')

@mod_user.route('/reset', methods=['POST'])
def re():
	username=request.form['username']
	newp=request.form['password']
	user=User.query.filter(User.username==username).first()
	user.password=newp
	db.session.commit()
	return redirect('/')

@mod_user.route('/user', methods=['POST'])
def get_users():
	print('in user')
	user=request.form['user']
	u=User.query.filter(User.username==user).first()
	if u:
		return "False"
	else:
		return "True"

@mod_user.route('/users', methods=['GET'])
def get():
	u=User.query.all()
	a=[]
	for i in u:
		a.append(i.username)
	return jsonify(a)


#@mod_user.route('/found', methods=['GET'])
#def found():
#	user = User.query.filter(User.username==session['user_name']).first()
#	return render_template('found.html', user=user)


