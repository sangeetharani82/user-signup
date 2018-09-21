from flask import Flask, request
import cgi
import os
import jinja2

template_dir = os.path.join(os.path.dirname(__file__), 'templates')
jinja_env = jinja2.Environment(loader = jinja2.FileSystemLoader(template_dir), autoescape=True)


app = Flask(__name__)
app.config['DEBUG'] = True


@app.route('/validate-data')
def display_data_form():
    template = jinja_env.get_template('data_form.html')
    return template.render(username='', name_error='', 
    userpswd='', pswd_error='', verifypswd='', v_pswd_error='', 
    useremail='', email_error='')


@app.route('/validate-data', methods=['POST'])
def validate_data():
    
    username = request.form['username']
    userpswd = request.form['userpswd']
    verifypswd = request.form['verifypswd']
    useremail = request.form['useremail']

    name_error = ''
    pswd_error = ''
    v_pswd_error = ''
    email_error = ''

    if len(username) < 3 or len(username) > 20 or not username.isalpha():
        name_error = "That's not a valid username"
        username = ''

    if len(userpswd) < 3 or len(username) > 20 or not userpswd.isalpha():
        pswd_error = "That's not a valid password"
        userpswd = ''
        
    if len(verifypswd) < 3 or len(verifypswd) > 20 or not verifypswd.isalpha() or userpswd != verifypswd:
        v_pswd_error = "Passwords don't match"
        verifypswd = ''

    
    if useremail == '':
        useremail = ''
    else:
        if useremail != '':
            if '@' not in useremail or '.' not in useremail:
                email_error = "That's not a valid email"
                useremail = ''

    if not name_error and not pswd_error and not v_pswd_error and not email_error:
        template= jinja_env.get_template('welcome_msg.html')
        return template.render(username=username)
    else:
        return data_form.format(name_error=name_error, 
        pswd_error=pswd_error, v_pswd_error=v_pswd_error, email_error=email_error, username=username,
        userpswd=userpswd, verifypswd=verifypswd, useremail=useremail)

@app.route("/")
def index():
    return form

app.run()