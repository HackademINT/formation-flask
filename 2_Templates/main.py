from flask import Flask
from flask import render_template
from flask import render_template_string
app = Flask(__name__)


@app.route("/")
def index():
    ligne1 = "<a href='{{ url_for('premierTemplate') }}'>Premier Template</a> </br>"
    ligne2 = "<a href='{{ url_for('deuxiemeTemplate') }}'>Deuxième Template</a>"
    return render_template_string(ligne1+ligne2)

@app.route("/theme1")
def premierTemplate():
    return render_template('startbootstrap.html',
            message="Formation Flask :D")

@app.route("/theme2")
def deuxiemeTemplate():
    return render_template('w3schools.com.html',
            message="Formation Flask :D")

if __name__ == "__main__":
    app.run()
