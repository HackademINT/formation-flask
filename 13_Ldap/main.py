"""
Documentation:
    https://www.python-ldap.org/en/latest/reference/ldap.html
"""
from flask import Flask
import ldap

app = Flask(__name__)

# A demander aux 2As ;-)
LDAP_PROVIDER_URL = ''
BASE_DN = ''

def get_ldap_connection():
    """
    Créer seulement l'objet pour se connecter.
    Il n'effectue donc aucune connexion ici.
    La connexion s'effectuera au premier appel d'une
    méthode de conn ("lazy connect")
    """
    ldap.set_option(ldap.OPT_X_TLS_REQUIRE_CERT, ldap.OPT_X_TLS_NEVER)
    conn = ldap.initialize(LDAP_PROVIDER_URL)
    return conn

def search(disi_id):
    conn = get_ldap_connection()
    try:
        r = conn.search_s('uid=' + disi_id + ',' + BASE_DN, ldap.SCOPE_SUBTREE)
        conn.unbind_s()
        return r
    except ldap.SERVER_DOWN as e:
        # Impossible de contacter le serveur
        # on le notifie dans les logs
        app.logger.info(e)
        # On lève à nouveau
        # la même exception à un plus haut niveau
        raise
    except ldap.NO_SUCH_OBJECT:
        return None

def authenticate(username,password):
    conn = get_ldap_connection()
    # A demander aux 2As ;-)
    r = conn.simple_bind_s()
    # Lève une exception si les identifiants sont erronés
    conn.unbind_s()

@app.route("/")
def index():
    s = search("")
    return s

if __name__ == "__main__":
    app.run(debug=True)

