from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_login import LoginManager, UserMixin, login_user, login_required, logout_user, current_user


app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///database/ma_super_db.db'
app.config['SECRET_KEY'] = 'HackademINT<3'
db = SQLAlchemy(app)
login_manager = LoginManager()
login_manager.init_app(app)


class User(UserMixin,db.Model):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(80), unique=True, nullable=False)
    email = db.Column(db.String(120), unique=True, nullable=False)

    def __repr__(self):
        return '<User %r>' % self.username

@login_manager.user_loader
def load_user(user_id):
    return User.query.get(int(user_id))

@app.route('/login')
def login():
    user = User.query.filter_by(username='nainA').first()
    login_user(user)
    return 'You are now logged in!'

@app.route('/')
@login_required
def index():
    return 'You can see this page because you are logged! The current user is ' + current_user.username

@app.route('/logout')
@login_required
def logout():
    logout_user()
    return 'You are now logged out!'

if __name__=='__main__':
    app.run()
