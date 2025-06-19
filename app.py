from flask import Flask, request, render_template, send_file, redirect, url_for, session
import pandas as pd
from main import my_web_scrapper
from flask_sqlalchemy import SQLAlchemy
from flask_login import LoginManager, login_user, logout_user, login_required, UserMixin
from datetime import datetime
# from app import db
# from app import app, db
# from models import User

app = Flask(__name__, static_url_path='/static', static_folder='static')
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///web_sc.db'  # Change to your database URI
app.secret_key = 'your_secret_key'
# # app.config['SQLALCHEMY_TRACK_MODIFICATIONS']= False
db = SQLAlchemy(app)

login_manager = LoginManager()
login_manager.init_app(app)

@login_manager.user_loader
def load_user(user_id):
    # Query the database for the user with the given ID
    return User.query.get(int(user_id))

class User(UserMixin, db.Model):
    id = db.Column(db.Integer, primary_key=True)
    email = db.Column(db.String(120), unique=True, nullable=False)
    password = db.Column(db.String(60), nullable=False)
    date_registered = db.Column(db.DateTime, nullable=False, default=datetime.utcnow)

    def __repr__(self):
        return f"User('{self.email}', '{self.date_registered}')"
    
@app.route('/')
def hello_world():
 return render_template ("home.html")

@app.route('/login')
def login():
#  email = request.form['email']
#  password = request.form['password']
#  user = User.query.filter_by(email=email).first()
#  if user and user.password == password:
#         # Log the user in
#         login_user(user)
#         # Redirect to some protected page
#         return redirect('/protected')
#  else:
#         # Handle invalid login
#         return render_template('login.html', error='Invalid email or password')
 return render_template('login.html') 
     
# @app.route('/protected')
# @login_required
# def protected_route():
#     # Only accessible to logged-in users
#     return render_template('protected.html')

# @app.route('/logout')
# @login_required
# def logout():
#     logout_user()
#     return redirect('/index')

@app.route('/index')
def index():
 return render_template('index.html')
                             
@app.route('/register', methods=['GET','POST'])
def register():
    if request.method == 'POST':
        email = request.form['email']
        password = request.form['password']
        # Create a new user object
        new_user = User(email=email, password=password)
        # Add the new user to the database session
        db.session.add(new_user)
        # Commit the changes to the database
        db.session.commit()
        return redirect('/index') 
    return render_template('register.html')

@app.route('/scrape', methods=['POST'])
def scrape():
 url = request.form.get('url')
 my_web_scrapper(url)
 return send_file('data.csv', as_attachment=True)

@app.route('/data-viewer')
def data_viewer():
    # Read the CSV file into a DataFrame
    df = pd.read_csv('data.csv')
    # Convert the DataFrame to HTML format
    data_html = df.to_html()
    return render_template('data_viewer.html', data_html=data_html)

if __name__ == "__main__":
    with app.app_context():
        db.create_all()
        print("Database tables created successfully.")
    app.run(debug=True)