from flask import Flask, session

from checker import check_logged_in

app = Flask(__name__)

app.secret_key = 'ihavetoSetthisKindofString'

@app.route('/')
def hello() -> str:
    return 'Hello from the simple webapp'

@app.route('/login')
def login() -> str:
    session['logged_in'] = True
    return 'You are now logged in'

@app.route('/logout')
def logout() -> str:
    session.pop('logged_in')
    return 'You are now logged out'

@app.route('/page1')
@check_logged_in
def page1() -> str:
    return 'This is page 1'

@check_logged_in
@app.route('/page2')
def page2() -> str:
    return 'This is page 2'

@check_logged_in
@app.route('/page3')
def page3() -> str:
    return 'This is page 3'

if __name__ == '__main__':
    app.run(debug=True)