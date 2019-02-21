from flask import Flask
from myapp.simple_page import simple_page

app = Flask(__name__)
app.register_blueprint(simple_page, url_prefix='/pages')

@app.route('/')
def home():
    return "Ok"

if __name__ == "__main__":
    app.run(debug=True)
