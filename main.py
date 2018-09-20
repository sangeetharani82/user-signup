from flask import Flask, request
import cgi

app = Flask(__name__)
app.config['DEBUG'] = True


data_form = """
    <style>
        .error {{ color: red;}}
    </style>
    <h1>Signup</h1>
    <form method='POST'>
        <label>Username
            <input name="user-name" type="text" value='{user_name}' />
        </label>
        <p class="error">{name_error}</p>
        <label>Password
            <input name="user-pswd" type="password" value='{password}'/>
        </label>
        <p class="error">{pswd_error}</p>
        <label>Verify Password
            <input name="verify-pswd" type="password" value='{v_pswd}' />
        </label>
        <p class="error">{v_pswd_error}</p>
        <label>Email(optional)
            <input name="user-email" type="text" value='{email}' />
        </label>
        <p class="error">{email_error}</p>
        <input type="submit" value="Submit" />
    </form>

"""

@app.route('/validate-data')
def display_data_form():
    return data_form.format(user_name='', name_error='', 
    password='', pswd_error='', v_pswd='', v_pswd_error='', 
    email='', email_error='')

def is_alpha(str_input):
    try:
        (str_input).isalpha()
        return True
    except ValueError:
        return False


@app.route('/validate-data', methods=['POST'])
def validate_data():
    
    user_name = request.form['user_name']
    user_pswd = request.form['password']
    user_v_pswd = request.form['v_pswd']
    user_email = request.form['email']

    name_error = ''
    pswd_error = ''
    v_pswd_error = ''
    email_error = ''

    if not is_alpha(user_name):
        name_error = "That's not a valid username"
        user_name = ''
    else:
        if len(user_name) < 3 or len(user_name) > 20:
            name_error = "That's not a valid username"
            user_name = ''

    if not is_alpha(user_pswd):
        pswd_error = "That's not a valid password"
        user_pswd = ''
    else:
        if len(user_pswd) < 3 or len(user_name) > 20:
            pswd_error = "That's not a valid password"
            user_pswd = ''
        
    if not is_alpha(user_v_pswd):
        v_pswd_error = "Passwords don't match"
        user_v_pswd = ''
    else:
        if len(user_v_pswd) < 3 or len(user_v_pswd) > 20 or user_pswd != user_v_pswd:
            v_pswd_error = "Passwords don't match"
            user_v_pswd = ''

    if not is_alpha(user_email):
        email_error = "That's not a valid email"
        user_email = ''
    else:
        if '@' not in user_email or '.' not in user_email:
            email_error = "That's not a valid email"
            user_email = ''

    if not name_error and not pswd_error and not v_pswd_error and not email_error:
        return "<h1>Welcome " + user_name + "!</h1>"
    else:
        return data_form.format(name_error=name_error, 
        pswd_error=pswd_error, v_pswd_error=v_pswd_error, email_error=email_error, user_name=user_name,
        user_pswd=user_pswd, user_v_pswd=user_v_pswd, user_email=user_email)

@app.route("/")
def index():
    return form

app.run()