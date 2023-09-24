# Import the Flask class from the flask module
from flask import Flask, render_template, redirect, url_for, request, flash
from flask_login import LoginManager, UserMixin, login_user, login_required, logout_user, current_user
import os
import cred

# Create an instance of the Flask class
app = Flask(__name__)
# Set a secret key for your Flask app
app.secret_key = cred.SECRET_WORD
print(app.secret_key)
# Initialize Flask-Login
login_manager = LoginManager()
login_manager.init_app(app)

# Define a User model
class User(UserMixin):
    def __init__(self, id):
        self.id = id

# Define a user loader function (used by Flask-Login)
@login_manager.user_loader
def load_user(user_id):
    return User(user_id)


# Define a route and a function to handle the route
@app.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        user_id = request.form['user_id']  # Replace with your actual form field name
        user = User(user_id)
        login_user(user)
        flash('Logged in successfully!', 'success')
        return redirect(url_for('dashboard'))
    return render_template('login.html')

@app.route('/logout')
@login_required
def logout():
    logout_user()
    flash('Logged out successfully!', 'success')
    return redirect(url_for('login'))

@app.route('/dashboard')
@login_required
def dashboard():
    return render_template('dashboard.html')


# Run the application if this script is executed
if __name__ == '__main__':
    print('running')
    app.run()
