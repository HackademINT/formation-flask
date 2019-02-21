from flask import Flask
from flask_mail import Mail, Message
from threading import Thread

app = Flask(__name__)

app.config['MAIL_SERVER'] = 'XXXXXXXXXXXXXX'
app.config['MAIL_DEFAULT_SENDER'] = 'XXXXXX <XXXXXXXXX@XXXXXXX>' #Optionnel
USERS = ["XXXXXXXXXXX <XXXXXX@XXXXXXXX"]


mail = Mail(app)


def sendMail(subject, message, users=USERS):
    with mail.connect() as conn:
        for user in users:
            msg = Message(subject, recipients=[user])
            msg.html = ""
            msg.html += "<p>" + str(message) + "</p>"
            try:
                conn.send(msg)
            except:
                app.logger.info("Impossible d'envoyer un mail à " + str(user))
                app.logger.info(sys.exc_info()[0])
    return True

@app.route("/")
def index():
    sendMail("Mon Sujet", "Mon message", users=USERS)
    return "OK"

if __name__ == "__main__":
    app.run(debug=True)
