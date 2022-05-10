#!C:/user/sahithi/AppData/Roaming/Microsoft/Windows/Start Menu/Programs/Python 3.8


print("Content-Type:text/html")
print()
import cgi

print("<h1>welcome to python</h1>")
print("<hr/>")
print("<h1>using input tag</h1>")
print("<body bgcolor='red'>")

form=cgi.FieldStorage()

id=form.getvalue("id")
name=form.getvalue("name")
gender=form.getvalue("gender")
age=form.getvalue("age")
number=form.getvalue("number")
db=form.getvalue("date of birth")
address=form.getvalue("address")
Qualification=form.getvalue("Qualification")





import mysql.connector

con=mysql.connector.connect(user='root',password='',host='localhost',database='python')
cur=con.cursor(buffered=True)


cur.execute("insert into info values(%s,%s,%s,%s,%s,%s,%s,%s)",(id,name,gender,age,number,db,address,Qualification))
#cur.execute("insert info")
con.commit()
cur.close()
con.close()



print("<h3>record inserted successfully</h3>")
