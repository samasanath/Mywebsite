from flask import Flask, render_template, redirect, url_for, request

app = Flask(__name__,template_folder="template",instance_relative_config=True)


import mysql.connector
from mysql.connector import errorcode
import cgi
import cgitb
cgitb.enable()

form=cgi.FieldStorage()


#@app.route('/about', methods=['GET', 'POST'])
#def login():
#	if request.method == 'POST':
#		id=request.form['id']
#		name=request.form['name']
#		con=mysql.connector.connect(user='root',password='',host='localhost',database='my_first_db')
#		cur=con.cursor()
#		cur.execute("INSERT INTO student VALUES(%s,%s)",(id,name))
#		con.commit()
#		cur.close()
#		con.close()
#		return redirect(url_for('done'))
#	return render_template('first.html')


@app.route('/')
def home():
	con=mysql.connector.connect(user='root',password='',host='localhost',database='my_first_db')
	cur=con.cursor()
	cur.execute('SELECT * FROM student')
	#cur.execute('SELECT * FROM student WHERE id = %s AND name = %s', (id,name))
	result=cur.fetchall()
	for x in result:
		print (x)
	con.commit()
	cur.close()
	con.close()
	return render_template('new.html',value=result )



@app.route('/about')
def done():
	return "done your registeration"

