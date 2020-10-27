from flask import Flask, render_template, request, session, url_for, redirect
# Forms
from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField, BooleanField, RadioField, SelectField, TextAreaField
from wtforms.validators import DataRequired, Length

from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate

from config import DevConfig


# Nome progetto
corso = Flask(__name__)
# Necessaria per gestire i forms
corso.secret_key="supersecret"
#SQL Alchemy
corso.config.from_object(DevConfig)

db = SQLAlchemy(corso)
migrate = Migrate(corso, db)

class Corso(db.Model):
    id = db.Column(db.Integer(), primary_key=True)
    titolo = db.Column(db.String(100), unique=True, nullable=False)
    descrizione = db.Column(db.String(255))
    insegnante = db.Column(db.String(100))
    livello = db.Column(db.String(50))
    serate = db.relationship('Serata', backref='corso', lazy='subquery')

    def __init__(self,titolo,descrizione,insegnante,livello):
        self.titolo=titolo
        self.descrizione=descrizione
        self.insegnante=insegnante
        self.livello=livello

    def __repr__(self):
        return "{}:{} è tenuto da {}".format(
            self.titolo,
            self.descrizione,
            self.insegnante
        )

class Serata(db.Model):
    id = db.Column(db.Integer(), primary_key=True)
    descrizione = db.Column(db.String(255), nullable=False)
    data = db.Column(db.DateTime())
    corso_id = db.Column(db.Integer(), db.ForeignKey('corso.id'))
    
    def __init__(self, descrizione, data):
        self.descrizione = descrizione
        self.data = data

    def __repr__(self):
        return "<Descrizione '{}'>".format(self.descrizione)


def index():
    user_agent = request.headers.get('User-Agent')
    return render_template('index.html', user_agent=user_agent)
# Altro modo per fare routing
# add_url_rule: the URL, the endpoint name, and the view function
corso.add_url_rule('/', 'index', index)


''' 
LEZIONE 2

SIMPLE FORM WITH GET - A scopo didattico
Routing ad una form di prova usando GET con output sulla stessa pagina
Metodo sconsigliato
'''
@corso.route("/prova_get_stessa")
def prova_get_stessa():
    # Richiama i campi con get
    campo_uno=request.args.get("campo-uno")
    campo_due=request.args.get("campo-due")
    # Richiamo template
    return render_template("get_stessa_pagina.html",campo_uno=campo_uno, campo_due=campo_due)

'''
A scopo didattico
Routing ad una form di prova usando GET con output sulla pagina differente
Metodo sconsigliato
'''
@corso.route("/prova_get_altra")
def prova_get_altra():
    # Richiamo template
    return render_template("get_altra_pagina.html")

@corso.route("/prova_get_altra_output")
def prova_get_altra_output():
    # Richiama i campi con get
    campo_uno=request.args.get("campo-uno")
    campo_due=request.args.get("campo-due")
    # Richiamo template
    return render_template("get_altra_pagina_output.html",campo_uno=campo_uno, campo_due=campo_due)

'''
SIMPLE FORM WITH POST - A scopo didattico
Routing ad una form di prova usando POST con output sulla stessa pagina
'''
# Definizione form ereditando da FlaskForm
class PostBase(FlaskForm):
    campo_uno = StringField("Campo uno (*)",validators=[DataRequired()])
    campo_due = StringField("Campo due")
    submit = SubmitField("Conferma")

@corso.route("/prova_post_stessa", methods=["GET","POST"])
def prova_post_stessa():
    post_form = PostBase()
    # Servono????
    # campo_uno=False
    # campo_due=False
    # Al submit recupero le info
    if post_form.validate_on_submit():
        campo_uno = post_form.campo_uno.data
        campo_due = post_form.campo_due.data
        # Reset
        post_form.campo_uno.data = ""
        post_form.campo_due.data = ""

        return render_template(
            "post_stessa_pagina.html",
            post_form=post_form, 
            campo_uno=campo_uno, 
            campo_due=campo_due)
    # Richiamo template
    return render_template(
        "post_stessa_pagina.html",
        post_form=post_form
        )

'''
A scopo didattico
Routing ad una form di prova usando POST con output su ALTRA pagina
'''
@corso.route("/prova_post_altra", methods=["GET","POST"])
def prova_post_altra():
    post_form = PostBase()
    # Servono????
    # campo_uno=False
    # campo_due=False
    # Richiamo template
    if post_form.validate_on_submit():
        campo_uno = post_form.campo_uno.data
        campo_due = post_form.campo_due.data
        # Reset
        post_form.campo_uno.data = ""
        post_form.campo_due.data = ""
        #return render_template("post_altra_pagina_output.html",post_form=post_form, campo_uno=campo_uno, campo_due=campo_due)
        return redirect(url_for("prova_post_altra_output"))

    return render_template(
        "post_altra_pagina.html",
        post_form=post_form
    )

@corso.route("/prova_post_altra_output", methods=["GET","POST"])
def prova_post_altra_output():
    # Get values from form
    campo_uno = request.form.get('campo_uno')
    campo_due = request.form.get('campo_due')
    # Richiamo template
    return render_template(
        "post_altra_pagina_output.html",
        campo_uno=campo_uno,
        campo_due=campo_due
    )

# LEZIONE 1
# Decoratore rotta: indirizzo pagina web
@corso.route("/corsi")
def corsi():
    lista_corsi = { 'Flask':'Corso in 5 lezioni di Andrea', 
                    'PyGame':'Piccoli approfondimenti da Mario', 
                    'Numpy':'Cenni di Data Science da Maria Teresa' }
    return render_template('lista.html', lista_corsi=lista_corsi, title="Corsi Python Group Biella")

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






'''
Tentativi lezione 2
'''
# Definizione form con elenco campi
class CorsoForm(FlaskForm):
    titolo = StringField("Nome del corso",validators=[DataRequired(),Length(max=100)])
    descrizione = StringField("Descrizione del corso",validators=[DataRequired(),Length(max=255)])
    insegnante = StringField("Docente del corso",validators=[DataRequired(),Length(max=100)])
    # corso_attivo = BooleanField("Corso attivo")
    livello = RadioField("Livello", choices=[('easy','Facile'),('intermediate','Intermedio'),('pro','Pro')])
    # piattaforma = SelectField(u"Piattaforma online",choices=[('zoom','Zoom'),('teams','Teams'),('meet','Meet')])
    # feedback = TextAreaField()
    submit = SubmitField("Conferma")

@corso.route("/corsi/<int:corso_id>", methods=["GET","POST"])
def crea_corso(corso_id):
    form = CorsoForm()

    # Al submit recupero le info
    if form.validate_on_submit():
        nuovo_corso = Corso()
        nuovo_corso.titolo = form.titolo.data
        nuovo_corso.descrizione = form.descrizione.data
        nuovo_corso.insegnante = form.insegnante.data
        nuovo_corso.livello = form.livello.data
        nuovo_corso.id = corso_id
        try:
            db.session.add(nuovo_corso)
            db.session.commit()
        except Exception as e:
            flash('Errore durante l''inserimento del corso:  %s' % str(e), 'error')
            db.session.rollback()
        else:
            flash('Corso aggiunto', 'info')

        return redirect(url_for("corsi",corso_id=corso_id))
    
    corso = Corso.query.get_or_404(corso_id)
    serate = corso.serate

    return render_template("corso.html",course_form=form, corso=corso, serate=serate)

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

# Lezione 1
# Gestore errori
@corso.errorhandler(404)
def page_not_found(error):
    return render_template('404.html'),404

if __name__ == "__main__":
    corso.run(debug=True)