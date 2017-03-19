
from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask import render_template

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql://postgres:Joshua123@localhost/flasktest'
db = SQLAlchemy(app)

class User(db.Model):
	id = db.Column(db.Integer, primary_key=True)
	username = db.Column(db.String(80), unique=True)
	email = db.Column(db.String(120), unique=True)

	def __init__(self, username, email):
		self.username = username
		self.email = email

	def __repr__(self):
		return '<User %r>' % self.username

@app.route('/')
def index():
	return render_template('add_user.html',

@app.route('/post_user', methods=['POST'])
def post_user():
	return "<h1 style='color: red'>Hello World!</h1>"

if __name__ == "__main__":
	app.run()