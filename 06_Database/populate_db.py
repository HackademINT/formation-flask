from main import db
from main import User

user1 = User(username='nainA', email='supertoto@example.com')
user2 = User(username='nainB', email='supertata@example.com')

db.session.add(user1)
db.session.add(user2)

db.session.commit()

print(User.query.all())

print(User.query.filter_by(username='nainA').first())
