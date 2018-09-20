from flask import Flask, request
import cgi

app = Flask(__name__)
app.config['DEBUG'] = True


form ="""
<!doctype html>
<html>
    <body>
        
        <h1>Signup</h1>
        <form action="/signup" method="post">
            <label for="user-name">Username
                <input id="user-name" type="text" name="user-name"/>
            </label>
            <br>
            <label for="password">Password
                <input id="password" type="password" name="user-password"/>
            </label>
                <br>
            <label for="verify-pswd">Verify Password
                <input id="verify-pswd" type="password" name="verify-password"/>
            </label>
                <br>
            <label for="email">Email(optional)
                <input id="email" type="text" name="user-email"/>
                </label>
                <br>
            <input type="submit" value="Submit"/>
            
        </form>
    </body>
</html>
"""

data_form = """
    <style>
        .error {{ color: red;}}
    </style>
    <h1>Signup</h1>
    <form method='POST'>
        <label>Username
            <input name="user-name" type="text" value='{name}' />
        </label>
        <p class="error">{name_error}</p>
        <label>Password
            <input name="user-pswd" type="password" value='{password}'/>
        </label>
        <p class="error">{pswd_error}</p>
        <label>Verify Password
            <input name="verify-pswd" type="password" value='{v_pswd}' />
        </label>
        <p class="error>{v_pswd_error}</p>
        <label>Email (optional)
            <input name="user-email" type="text" value='{user_email}' />
        </label>
        <p class="error">{email_error}</p>
        
        
        <input type="submit" value="Submit" />
    </form>

"""

@app.route('/validate-data')
def display_data_form():
    return data_form.format(name='', name_error='', 
    password='', pswd_error='', v_pswd='', v_pswd_error='', 
    user_email='', email_error='')

@app.route("/")
def index():
    return form

@app.route("/signup", methods=['POST'])
def signup():
    user_name = request.form['user-name']
    return "<h1>Welcome " + user_name + "!</h1>"
    

app.run()