from flask import Flask, render_template
app = Flask(__name__)


class Voiture:
    def __init__(self, marque, modele, couleur, places):
        self.marque = marque
        self.modele = modele
        self.couleur = couleur
        self.places = places

VILLES = ['Paris', 'Londres', 'Madrid', 'Metz']

def mesVoitures():
    t = []
    renault = Voiture("Renault", "Laguna", "Bleu", "5")
    peugeot = Voiture("Peugeot", "307", "Rouge", "5")
    volkswagen = Voiture("Volkswagen", "Golf", "Gris vraiment stylé", "5")
    t.append(renault)
    t.append(peugeot)
    t.append(volkswagen)
    return t

@app.route("/")
def hello():
    message = "Un beau template :D"
    t = mesVoitures()
    return render_template('index.html', message=message,
            villes=VILLES, voitures=t)

if __name__ == "__main__":
    app.run()
