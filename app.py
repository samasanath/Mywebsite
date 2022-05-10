from flask import Flask,render_template
app = Flask(__name__, template_folder="template")
@app.route("/")
def index():
	return render_template("intex.html")
@app.route("/about")
def fan():
	return "<h1>hi iam sanath.....!</h1>"
if __name__ == '__main__':
	app.run()

