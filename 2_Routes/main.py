from flask import Flask, abort
app = Flask(__name__)

@app.route("/")
def hello():
    return "Hello World!"

@app.route('/user/<username>')
def show_user_profile(username):
    return 'User %s' % username

@app.route('/post/<int:post_id>')
def show_post(post_id):
    return 'Post %d' % post_id

@app.route('/path/<path:subpath>')
def show_subpath(subpath):
    return 'Subpath %s' % subpath

# Error
@app.errorhandler(404)
def erreur404(error):
    return "Il n'y a rien ici",404


if __name__ == "__main__":
    app.run()
