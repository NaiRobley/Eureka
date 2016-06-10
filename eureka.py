# -*- coding: utf-8 -*-
#!/usr/bin/env python

# requires python 2.7+

## to install flask
# pip install flask for python 2
# pip3 install flask for python 3

## to install MySQLdb
# apt-get install python-mysqldb

## to install pdfkit
# pip install pdfkit
# pip3 install pdfkit
# Password encryption avoided for testing purposes

from flask import Flask, render_template, request, redirect, json, session
from flask.ext.mysql import MySQL
from flask.ext.uploads import UploadSet, IMAGES, configure_uploads
import MySQLdb, time, os, uuid, sys, json

__author__ = 'Robley < robleyadrian@gmail.com >'

eureka = Flask(__name__)

eureka.secret_key = 'secret'

mysql = MySQL()

# Database configuration
eureka.config['MYSQL_DATABASE_USER'] = 'root'
eureka.config['MYSQL_DATABASE_PASSWORD'] = 'toor'
eureka.config['MYSQL_DATABASE_DB'] = 'eureka'
eureka.config['MYSQL_DATABASE_HOST'] = 'localhost'
eureka.config['UPLOADED_PHOTOS_DEST'] = '../static/uplds'

mysql.init_app (eureka)

# Home page
@eureka.route('/')
def home_page():
	return render_template ('index.html')

# Login / Register Page
@eureka.route('/logreg')
def logreg():
	return render_template('logreg.html')

# Register
@eureka.route('/reg', methods=['POST'])
def reg():
	fname = request.form['fname']
	lname = request.form['lname']
	gender = request.form['gender']
	username = request.form['username']
	password = request.form['password']
	email = request.form['email']

	conn = mysql.connect()
	curr = conn.cursor()

	curr.execute("""INSERT INTO users(fname, lname, email, gender, u_name, password) VALUES(%s,%s,%s,%s,%s,%s)""",(fname, lname, email, gender, username, password))
	conn.commit()
	conn.close()

	res = "Your details have been submitted successfully. You can now login"
	return render_template('logreg.html', msg2=res)

# Login
@eureka.route('/login', methods=['POST'])
def login():
	username = request.form['username']
	password = request.form['password']

	cur = mysql.connect().cursor()

	cur.execute("""SELECT * FROM users WHERE u_name=%s AND password=%s""",(username, password))
	data = cur.fetchall()
	if len(data)>0:
		nme = data[0][1]
		nme2 = data[0][2]

		session['user'] = data[0][0]

		x = session.get('user')

		return render_template('home.html', msg = 'You are now at home', nme=nme+' '+nme2)
	else:
		res = "Wrong username or password. Try again."
		return render_template('logreg.html',msg=res)

@eureka.route('/admin_login')
def admn():
	return render_template('admin_login.html')

# admin login
@eureka.route('/adminloginpg', methods=['POST'])
def admin_login():
	username = request.form['username']
	password = request.form['password']

	cur = mysql.connect().cursor()

	cur.execute("""SELECT * FROM admins WHERE auname=%s AND apasswd=%s""",(username, password))
	data = cur.fetchall()
	if len(data)>0:
		nme = data[0][1]

		session['user'] = data[0][0]

		x = session.get('user')

		return render_template('adminhome.html', msg = 'You are now at home admin', nme=nme)
	else:
		res = "Wrong username or password. Try again."
		return render_template('logreg.html',msg=res)

# admin home
@eureka.route('/report')
def report():
	if session.get('user'):

		cur = mysql.connect().cursor()
		cur.execute("""SELECT * FROM admins""")
		data1 = cur.fetchall()
		admin_dict = []
		for admn in data1:
			admindict = {'username':admn[1],'email':admn[3]}
			admin_dict.append(admindict)

		cur2 = mysql.connect().cursor()
		cur2.execute("""SELECT * FROM users""")
		data2 = cur2.fetchall()
		user_dict = []
		for usr in data2:
			usrdict = {'fname':usr[1],'lname':usr[2],'email':usr[3],'gender':usr[4],'username':usr[5]}
			user_dict.append(usrdict)

		cur3 = mysql.connect().cursor()
		cur3.execute("""SELECT * FROM categories""")
		data3 = cur3.fetchall()
		cat_dict = []
		for cat in data3:
			catdict = {'name':cat[1],'desc':cat[2]}
			cat_dict.append(catdict)


		cur4 = mysql.connect().cursor()
		cur4.execute("""SELECT * FROM projects""")
		data4 = cur4.fetchall()
		prjct_dict = []
		for pr in data4:
			y = int(pr[3])
			if y == 1:
				pcat = 'Computer Science'
			elif y == 2:
				pcat = 'Business'
			elif y == 3:
				pcat = 'Engineering'
			elif y == 4:
				pcat = 'Other'
			else:
				pcat = 'Undefined'

			prjdct = {'name':pr[1],'desc':pr[2], 'category':pcat}
			prjct_dict.append(prjdct)

		
		return render_template('report.html', user_dict = user_dict, cat_dict = cat_dict,prjct_dict = prjct_dict, admin_dict = admin_dict)
	else:
		render_template('error.html', msg='Please Log in as the administrator to view this page')

@eureka.route('/pdfroute')
def pdfgen():
	pass

# Home Page
@eureka.route('/home')
def homepage():
	if session.get('user'):
		return render_template ('home.html')
	else:
		return render_template ('error.html', msg='Please log in or register first to view this page')

# Projects Page
@eureka.route('/project')
def prjct():
	if session.get('user'):
		return render_template('prjcts.html')
	else:
		return render_template('error.html', msg='Please log in or register first to view this page')

# Categories Page
@eureka.route('/categories')
def categories():
	if session.get('user'):
		cr = mysql.connect().cursor()
		cr.execute("""SELECT * FROM categories""")
		dta = cr.fetchall()
		if len(dta)>0:
			cat1 = dta[0][1]
			dcat1 = dta[0][2]
			cat2 = dta[1][1]
			dcat2 = dta[1][2]
			cat3 = dta[2][1]
			dcat3 = dta[2][2]
			cat4 = dta[3][1]
			dcat4 = dta[3][2]
		return render_template('categories.html', cat1=cat1, dcat1=dcat1, cat2=cat2, dcat2=dcat2, cat3=cat3, dcat3=dcat3, cat4=cat4, dcat4=dcat4)
	else:
		return render_template('error.html', msg='Please log in or register first to view this page')

# Single Category Projects
@eureka.route('/cat_spec', methods=['POST'])
def cat_spec():
	if session.get('user'):
		if request.form['cat_id'] == "Computer Science Projects":
			crr = mysql.connect().cursor()
			crr.execute("""SELECT * FROM projects WHERE c_id=1""")
			dtat = crr.fetchall()

			projects_dict = []
			for proj in dtat:
				proj_dict = {'Name': proj[1],'Desc': proj[2]}
				projects_dict.append(proj_dict)

			return render_template('cat_spec.html', cat = 'Computer Science Projects', cat_name = 'Computer Science Projects', proj_dict = projects_dict)

		elif request.form['cat_id'] == "Business Projects":
			crrs = mysql.connect().cursor()
			crrs.execute("""SELECT * FROM projects WHERE c_id=2""")
			dtat = crrs.fetchall()

			projects_dict = []
			for proj in dtat:
				proj_dict = {'Name': proj[1],'Desc': proj[2]}
				projects_dict.append(proj_dict)

			return render_template('cat_spec.html', cat = 'Business Projects', cat_name = 'Business Projects', proj_dict = projects_dict)


		elif request.form['cat_id'] == "Engineering Projects":
			crrs = mysql.connect().cursor()
			crrs.execute("""SELECT * FROM projects WHERE c_id=3""")
			dtat = crrs.fetchall()
			projects_dict = []
			for proj in dtat:
				proj_dict = {'Name': proj[1],'Desc': proj[2]}
				projects_dict.append(proj_dict)
			return render_template('cat_spec.html', cat = 'Engineering Projects', cat_name = 'Engineering Projects', proj_dict = projects_dict)

		elif request.form['cat_id'] == "Other Projects":
			crrs = mysql.connect().cursor()
			crrs.execute("""SELECT * FROM projects WHERE c_id=4""")
			dtat = crrs.fetchall()
			projects_dict = []
			for proj in dtat:
				proj_dict = {'Name': proj[1],'Desc': proj[2]}
				projects_dict.append(proj_dict)

			return render_template('cat_spec.html', cat = 'Other Projects', cat_name = 'Other Projects', proj_dict = projects_dict)

	else:
		return render_template('error.html', msg='Please log in or register first to view this page')

# Specific Projects
# @eureka.route('/prjct')
# def prjct():
# 	pass

# Profile Page
@eureka.route('/profile')
def profile():
	if session.get('user'):
		x = session.get('user')
		x = str(x)

		cur = mysql.connect().cursor()

		cur.execute("""SELECT * FROM users WHERE u_id=%s""",(x))
		data = cur.fetchall()
		if len(data)>0:
			nme = data[0][1]
			nme2 = data[0][2]
			email = data[0][3]
			gender = data[0][4]
			username = data[0][5]

		cur.execute("""SELECT * FROM projects WHERE u_id=%s""",(x))
		dt = cur.fetchall()

		if len(dt)>0:
			prof_dict = []

			for p in dt:
				pfdct = {'name':p[1],'desc':p[2]}
				prof_dict.append(pfdct)

		elif len(dt)==0:
			prof_dict = [{'name':'Sorry','desc':'No projects available for this user'}]

		return render_template('profile.html', fname=nme, lname=nme2, email=email, gender=gender, username=username, prof_dict = prof_dict)
	else:
		return render_template('error.html', msg='Please log in or register first to view this page')

# New Project Page
@eureka.route('/new_proj')
def new_proj():
	if session.get('user'):
		return render_template('new_proj.html')
	else:
		return render_template('error.html', msg='Please log in or register first to view this page')

# Upload A New Project
@eureka.route('/uploadproject', methods=['POST'])
def uploadproject():
	y = session.get('user')
	pname = request.form['pname']
	pdesc = request.form['pdesc']
	c_id = request.form['category']

	con2 = mysql.connect()
	cur2 = con2.cursor()

	cur2.execute("""INSERT INTO projects(pname, pdesc, c_id, u_id) VALUES(%s,%s,%s,%s)""",(pname, pdesc, c_id, y))
	con2.commit()
	con2.close()

	return render_template('profile.html', msg='Your details have been submitted successfully.')

# Edit Profile Page
@eureka.route('/edit_profile')
def edit_profile():
	if session.get('user'):
		return render_template ('edit_profile.html')
	else:
		return render_template('error.html', msg='Please log in or register first to view this page')

# Submit New Profile Details
@eureka.route('/edit_prof', methods=['POST'])
def edit_prof():
	if session.get('user'):
		q = session.get('user')
		fname = request.form['fname']
		lname = request.form['lname']
		gender = request.form['gender']
		email = request.form['email']
		uname = request.form['username']
		passwd = request.form['password']

		conn = mysql.connect()
		curr = conn.cursor()

		curr.execute("""UPDATE users SET fname = %s, lname = %s, email = %s, gender = %s, u_name = %s, password = %s WHERE u_id = %s """,(fname,lname, email, gender, uname, passwd, q))
		conn.commit()
		conn.close()

		return render_template('profile.html', msg2 = "Your Profile Has Been Updated")

	else:
		return render_template('error.html', msg="Please log in register first to view this page")


# Logout
@eureka.route('/logout')
def logout():

	# delete session
	session.pop('user',None)
	msg = 'You have successfully logged out'
	return render_template('index.html', msg = msg)

@eureka.route('/error')
def errorpage():
	return render_template('error.html', msg='Please log in or register to view this page')

# Start The System
if __name__ == '__main__':
	eureka.run(debug=True, port=5001)
