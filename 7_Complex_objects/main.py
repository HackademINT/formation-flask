from flask import Flask
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///database/ma_super_db.db'
db = SQLAlchemy(app)

from classes import User, Post, Category
if __name__=='__main__':
    app.run()
