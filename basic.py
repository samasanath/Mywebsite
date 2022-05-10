from flask import Flask,render_template
app = Flask(__name__)

@app.route("/")
def fan():
	return "hi iam sanath.....!"
if __name__ == '__main__':
	app.run()