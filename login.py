from flask import Flask, render_template, redirect, url_for, request ,Response ,session, flash, json
import requests

app = Flask(__name__,template_folder="template",instance_relative_config=True)

import mysql.connector 
from mysql.connector import errorcode

import cgi
import re
app.secret_key = 'your secret key'
app.config['SECRET_KEY'] = 'cairocoders-ednalan'


def is_human(captcha_response):
    """ Validating recaptcha response from google server
        Returns True captcha test passed for submitted form else returns False.
    """
    secret = "6LfkGr8ZAAAAAMbiCE_uuWyPEFiKy1uAgVhggKzA"
    payload = {'response':captcha_response, 'secret':secret}
    response = requests.post("https://www.google.com/recaptcha/api/siteverify", payload)
    response_text = json.loads(response.text)
    return response_text['success']



form=cgi.FieldStorage()


@app.route('/', methods=['GET', 'POST'])
def login():
    sitekey = "6LfkGr8ZAAAAAGagOxCwAaZGu2FwpeW_4nUGCiyn"
    error = None
    if request.method == 'POST':
        #sitekey = "6LfL87wZAAAAACwZ-OyX3W2fnjhQUoN6mUOnZaTN"

        con=mysql.connector.connect(user='root' ,password='' ,host='localhost' ,database='python')
        #cur = mysql.connection.cursor(MySQLdb.cursors.DictCursor)
        cur=con.cursor()
        #cur.execute('SELECT * FROM userslist WHERE username=%s AND password =%S', (username,password))
        cur.execute('SELECT * FROM userslist WHERE username = %s AND password = %s', (request.form['username'],request.form['password']))
        account = cur.fetchone()
        if account:
            session['loggedin'] = True
            session['username'] = request.form.get("username")
            session['password'] = request.form.get("password")
            captcha_response = request.form.get("g-recaptcha-response")
            if is_human(captcha_response):
                status = "Detail submitted successfully."
                return redirect(url_for('home'))
                #return render_template('login.html',sitekey=sitekey,error=error)
            else:
                status = "Sorry ! Please Check Im not a robot."
                #return "Please Check Im not a robot."
                error= 'Please Check Im not a robot.'

        else:
            error= 'invalid username/password'
            #return "invalid username/password"
    return render_template('login.html',sitekey=sitekey,error=error)





@app.route('/registration',methods=['GET','POST']) 
def get_ses():
    if request.method == 'POST':
        name=request.form['name']
        username=request.form['username']
        password=request.form['password']
        con=mysql.connector.connect(user='root',password='',host='localhost',database='python')
        cur=con.cursor()
        cur.execute("INSERT INTO userslist VALUES(%s,%s,%s)",(name,username,password))
        con.commit()
        cur.close()
        con.close()
        return render_template('new user success.html',username=username)
    return render_template('new user.html')







@app.route('/login', methods=['GET','POST'])
def home():
    if request.method == 'POST':
        fname=request.form['fname']
        mname = request.form['mname']
        lname=request.form['lname']
        gender=request.form['gender'] 
        age=request.form['age']
        number=request.form['number']
        db=request.form['date of birth']
        address=request.form['address']
        Qualification=request.form['Qualification']
        image=request.form['image']
        con=mysql.connector.connect(user='root',password='',host='localhost',database='python')
        cur=con.cursor()
        cur.execute("INSERT INTO details VALUES(%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)",(fname,mname,lname,gender,age,number,db,address,Qualification,image))
        con.commit()
        cur.close()
        con.close()
        return render_template('2nd page.html',fname=fname,mname=mname,lname=lname,gender=gender,age=age,number=number,db=db,address=address,Qualification=Qualification,image=image)
    return render_template('1st page.html')


if __name__ == '__main__':
    app.run(debug=True)


#http://SAMASANATH.website2.me
