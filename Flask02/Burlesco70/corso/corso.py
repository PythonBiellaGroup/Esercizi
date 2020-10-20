from flask import Flask, render_template, request, session, url_for, redirect
# Forms
from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField, BooleanField, RadioField, SelectField, TextAreaField
from wtforms.validators import DataRequired

# Nome progetto
corso = Flask(__name__)

corso.secret_key="supersecret"

def index():
    user_agent = request.headers.get('User-Agent')
    return render_template('index.html', user_agent=user_agent)
# Altro modo per fare routing
# add_url_rule: the URL, the endpoint name, and the view function
corso.add_url_rule('/', 'index', index)


'''
A scopo didattico
Routing ad una form di prova usando get
Metodo sconsigliato
'''
@corso.route("/prova_get")
def prova_get():
    # Richiama i campi con get
    campo_uno=request.args.get("campo-uno")
    campo_due=request.args.get("campo-due")
    # Richiamo template
    return render_template("pagina_get.html",campo_uno=campo_uno, campo_due=campo_due)

# Decoratore rotta: indirizzo pagina web
@corso.route("/corsi")
def corsi():
    lista_corsi = { 'Flask':'Corso in 5 lezioni di Andrea', 
                    'PyGame':'Piccoli approfondimenti da Mario', 
                    'Numpy':'Cenni di Data Science da Maria Teresa' }
    return render_template('lista.html', lista_corsi=lista_corsi, title="Corsi Python Group Biella")

# Definizione form con elenco campi
class CorsoBase(FlaskForm):
    name = StringField("Nome del corso",validators=[DataRequired()])
    teacher = StringField("Docente del corso")
    corso_attivo = BooleanField("Corso attivo")
    difficolta = RadioField("Livello", choices=[('easy','Easy'),('intermediate','Intermediate'),('pro','Pro')])
    piattaforma = SelectField(u"Piattaforma online",choices=[('zoom','Zoom'),('teams','Teams'),('meet','Meet')])
    feedback = TextAreaField()
    submit = SubmitField("Conferma")

# Esempio di creazione form con session
@corso.route("/corsi/crea", methods=["GET","POST"])
def crea_corso():
    # Non è necessario inizializzare la sessione
    form = CorsoBase()

    # Al submit recupero le info
    if form.validate_on_submit():
        session["name"] = form.name.data
        session["teacher"] = form.teacher.data
        session["corso_attivo"] = form.corso_attivo.data
        session["difficolta"] = form.difficolta.data
        session["piattaforma"] = form.piattaforma.data
        session["feedback"] = form.feedback.data
        # Reset dei campi
        form.name.data = ""
        form.teacher.data = ""
        form.corso_attivo.data = ""
        form.difficolta.data = ""
        form.feedback.data = ""

        return redirect(url_for("risultato_corso"))

    return render_template("nuovo_corso.html",course_form=form)

# Esempio di creazione form dato per dato
@corso.route("/corsi/create", methods=["GET","POST"])
def create_corso():
    name = False
    teacher = False
    corso_attivo = False
    difficolta = False
    piattaforma = False
    feedback = False
    # Non è necessario inizializzare la sessione
    form = CorsoBase()

    # Al submit recupero le info
    if form.validate_on_submit():
        name = form.name.data
        teacher = form.teacher.data
        corso_attivo = form.corso_attivo.data
        difficolta = form.difficolta.data
        piattaforma = form.piattaforma.data
        feedback = form.feedback.data
        # Reset dei campi
        form.name.data = ""
        form.teacher.data = ""
        form.corso_attivo.data = ""
        form.difficolta.data = ""
        form.feedback.data = ""

    return render_template("nuovo_corso.html", course_form=form, name=name, teacher=teacher,
        corso_attivo=corso_attivo, difficolta=difficolta, piattaforma=piattaforma, feedback=feedback)



@corso.route("/corsi/risultato_corso")
def risultato_corso():
    return render_template("risultato_corso.html")

# Esempio di dynamic route
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
        return render_template('dettaglio_corso.html', corso=corso, sessioni=sessioni, title=corso)
    else:
        return render_template('corso_non_pianficato.html', corso=corso)

@corso.errorhandler(404)
def page_not_found(error):
    return render_template('404.html'),404

if __name__ == "__main__":
    corso.run(debug=True)