from flask import Flask, render_template, request, flash, redirect, url_for, json
import requests #pip install requests

app = Flask(__name__, template_folder='template')

app.config['SECRET_KEY'] = 'cairocoders-ednalan'

def is_human(captcha_response):
    """ Validating recaptcha response from google server
        Returns True captcha test passed for submitted form else returns False.
    """
    secret = "6LfL87wZAAAAAI_sBOWeMGiVJOp7upnRO3qTnibm"
    payload = {'response':captcha_response, 'secret':secret}
    response = requests.post("https://www.google.com/recaptcha/api/siteverify", payload)
    response_text = json.loads(response.text)
    return response_text['success']
 
@app.route("/", methods=["GET","POST"])
def contact():
    sitekey = "6LfL87wZAAAAACwZ-OyX3W2fnjhQUoN6mUOnZaTN"

    if request.method == "POST":
       
        captcha_response = request.form['g-recaptcha-response']
        
        if is_human(captcha_response):
            # Process request here
            status = "Detail submitted successfully."
        else:
             # Log invalid attempts
            status = "Sorry ! Please Check Im not a robot."

        flash(status)
        return redirect(url_for('contact'))

    return render_template("info.html", sitekey=sitekey)
  
if __name__ == '__main__':
 app.run(debug=True)