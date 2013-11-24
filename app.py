from flask import Flask, redirect, render_template
app = Flask(__name__)

@app.route('/')
def index():
    return redirect(url_for('static', filename='index.html'))


@app.route('/site<num>')
def site(num):
    # Works for /site01, /site02, /site03, etc.
    return render_template('site{0}.html'.format(num))


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