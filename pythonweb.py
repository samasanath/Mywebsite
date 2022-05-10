#!C:/user/sahithi/AppData/Roaming/Microsoft/Windows/Start Menu/Programs/Python 3.8

print("Content-Type:text/html")
print()


from flask import Flask, render_template, redirect, url_for, request

app = Flask(__name__,template_folder="template",instance_relative_config=True)

import mysql.connector 
from mysql.connector import errorcode
import cgi


form=cgi.FieldStorage()



@app.route('/', methods=['GET', 'POST'])
def login():
	if request.method == 'POST':
		id=request.form['id']
		name = request.form['name']
		gender=request.form['gender']
		age=request.form['age']
		number=request.form['number']
		db=request.form['date of birth']
		address=request.form['address']
		Qualification=request.form['Qualification']
		con=mysql.connector.connect(user='root',password='',host='localhost',database='python')
		cur=con.cursor()
		cur.execute("INSERT INTO info VALUES(%s,%s,%s,%s,%s,%s,%s,%s)",(id,name,gender,age,number,db,address,Qualification))
		con.commit()
		cur.close()
		con.close()
		return redirect(url_for('home'))
	return render_template('info.html')

@app.route('/about')
def home():
	return "record inserted successfully."



