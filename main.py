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
            <label for="user-name">Username</label>
                <input id="user-name" type="text" name="user_name"/>
                <br>
            <label for="password">Password</label>
                <input id="password" type="password" name="password"/>
                <br>
            <label for="verify-pswd">Verify Password</label>
                <input id="verify-pswd" type="password" name="password"/>
                <br>
            <label for="email">Email(optional)</label>
                <input id="email" type="text" name="email" />
                <br>
            <input type="submit" value="Submit"/>
            
        </form>
    </body>
</html>
"""


@app.route("/")
def index():
    return form

@app.route("/signup", methods=['POST'])
def signup():
    user_name = request.form['user_name']
    return "<h1>Welcome " + user_name + "!</h1>"

app.run()