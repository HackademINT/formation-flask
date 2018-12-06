from flask import Flask, render_template
from flask_menu import Menu, register_menu

app = Flask(__name__)
Menu(app=app)

@app.route("/")
@register_menu(app, '.index', 'Home', order=3)
def hello():
    return render_template('index.html')

def monPrenom():
    # username : parameter of function show_user_profile
    # for url_for
    return {'username':"Roger"}

@app.route('/user/<username>')
@register_menu(app, '.show_user_profile', 'User', active_when=lambda : True, endpoint_arguments_constructor=monPrenom)
def show_user_profile(username):
    return render_template('index.html')

@app.route("/toto")
@register_menu(app, '.toto', 'Toto', order=0)
def toto():
    return render_template('index.html')

if __name__ == "__main__":
    app.run()
