from flask import Flask, session

app = Flask(__name__)
app.secret_key = "TheSecretKey"

@app.route('/')
def hello() -> str:
    return 'Hello from the simple webapp.'

@app.route('/login')
def do_login() -> str:
    session['logged_in'] = True
    return 'you are now logged in'

@app.route('/status')
def check_status() -> str:
    if 'logged_in' in session:
        return 'you are currently logged in'
    else:
        return 'you are Not logged in'

@app.route('/logout')
def do_logout() -> str:
    session.pop('logged_in')
    return 'you are now logged out'
        

@app.route('/page1')
def page1() -> str:
    return 'This is page 1.'

@app.route('/page2')
def page2() -> str:
    return 'This is page 2.'

@app.route('/page3')
def page3() -> str:
    return 'This is page 3.'

if __name__ == '__main__':
    app.run(debug=True)