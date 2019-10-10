from flask import Flask, request, redirect, render_template
import cgi

app = Flask(__name__)
app.config['DEBUG'] = True 

#display form
@app.route('/', methods=['GET'])
def index():
    return render_template("index.html")   

#Set up form validation for user inputs
@app.route('/', methods=['POST'])
def validate_signup():

    username = request.form['username']
    password = request.form['password']
    verify_password = request.form['verify_password']
    email = request.form['email']

    username_error = ''
    password_error = ''
    verify_password_error = ''
    email_error = ''

#Check length of username
    if len(username) < 3 or len(username) > 20:
        username_error = 'Please choose a user name between 3-20 characters.'
        username = ''
#check for spaces in username    
    if username.count(' ') > 0:
            username_error = 'Please removes space from username'
            username = ''        
#Check length is between 3-20 characters
    if len(password) < 3 or len(password) > 20:
        password_error = 'Please choose a password between 3-20 characters'
        password = ''
#Check there are no spaces        
    if password.count(' ') > 0:
        password_error = 'Please remove space from password'
        password = ''    
#check passwords match
    if password != verify_password:
        verify_password_error = 'Passwords do not match'
 #check for email   
    if len(email) > 0:
        #check for valid email
        if not 0 > email.count('@') > 1 and not email.count('.') > 0:
            email_error = 'Please enter a valid email'
            email = ''          

    if not username_error and not password_error and not verify_password_error and not email_error:
        return redirect('/welcome?username={0}'.format(username))
    else:
        return render_template('index.html', username_error = username_error, username=username, password=password, password_error=password_error, verify_password=verify_password, verify_password_error=verify_password_error, email=email, email_error=email_error)       

#Once valid singup data provided, redirected to welcome page
@app.route('/welcome')
def valid_signin():
    username = request.args.get('username')
    return render_template('welcome.html', username=username)

app.run()