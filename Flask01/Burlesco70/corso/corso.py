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

@corso.route("/corsi")
def corsi():
    lista_corsi = { 'Flask':'Corso in 5 lezioni di Andrea', 
                    'PyGame':'Piccoli approfondimenti da Mario', 
                    'Numpy':'Cenni di Data Science da Maria Teresa' }
    return render_template('lista.html', lista_corsi=lista_corsi)

@corso.route("/corsi/<corso>")
def dettaglio_corso(corso):
    lista_sessioni = { 'Flask':['1 - Introduzione a Flask e ai web server con Jinja Base',
                                '2 - Jinja avanzato e Forms',
                                '3 - Flask con Database',
                                '4 - Large Flask Applications',
                                '5 - REST Backend e concetti avanzati'],
                       'PyGame':['1 - Introduction and simple graphics',
                                 '2 - Graphics, Sprites, Sounds',
                                 '3 - Games and show cases']}
    sessioni = lista_sessioni.get(corso,[])
    if sessioni:
        return render_template('dettaglio_corso.html', corso=corso, sessioni=sessioni)
    else:
        return render_template('corso_non_pianficato.html', corso=corso)

@corso.errorhandler(404)
def page_not_found(error):
    return render_template('404.html'),404

if __name__ == "__main__":
    corso.run(debug=True)