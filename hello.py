from flask import Flask, redirect, render_template
app = Flask(__name__)


@app.route('/hello/')
def hello(name=None):
   return render_template('hello.html', name=name)

#@app.route('/login', methods=['POST', 'GET'])
#def login():
#    error = None
#    if request.method == 'POST':
#        if valid_login(request.form['username'],
#                       request.form['password']):
#            return log_the_user_in(request.form['username'])
#        else:
#            error = 'Invalid username/password'
    # the code below is executed if the request method
    # was GET or the credentials were invalid
#    return render_template('login.html', error=error)

if __name__ == '__main__':
   app.run(debug=True)