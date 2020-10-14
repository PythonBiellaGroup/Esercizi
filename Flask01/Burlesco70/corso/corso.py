from flask import Flask, render_template

# Nome progetto
corso = Flask(__name__)

# Decoratore rotta: indirizzo pagina web
@corso.route("/")
def login():
    return render_template('index.html')

@corso.route("/index")
def index():
    return render_template('index.html')

@corso.route("/home")
def home():
    return f"<h2>Welcome to home page<h2>"


@corso.route("/corsi")
def corsi():
    lista_corsi = { 'Flask':'Corso in 5 lezioni di Andrea', 
                    'PyGame':'Piccoli approfondimenti da Mario', 
                    'Numpy':'Cenni di Data Science da Maria Teresa' }
    return render_template('lista.html', lista_corsi=lista_corsi)

@corso.route("/corsi/<name>")
def nome_ok(name):
    return f"<h2>Il mio nome {name}"

@corso.errorhandler(404)
def page_not_found(error):
    return render_template('404.html'),404

if __name__ == "__main__":
    corso.run(debug=True)