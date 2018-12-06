from flask import Flask, render_template
import datetime
app = Flask(__name__)

@app.route("/")
def hello():
    return render_template("index.html")

@app.route("/ajax")
def ajax():
    time = datetime.datetime.now()
    return "Je donne de l'Ajax à qui veut ! J'en ai déjà donné " + str(time)

if __name__ == "__main__":
    app.run()
