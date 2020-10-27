from flask import Flask, render_template, request, session, url_for, redirect
# Forms
from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField, BooleanField, RadioField, SelectField, TextAreaField
from wtforms.validators import DataRequired, Length

from flask_sqlalchemy import SQLAlchemy
from sqlalchemy.schema import UniqueConstraint
import sqlalchemy.dialects.sqlite
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

# Tabella di relazione N:N tra Corso e Tag
tags = db.Table(
    'corso_tags',
    db.Column('corso_id', db.Integer, db.ForeignKey('corso.id')),    
    db.Column('tag_id', db.Integer, db.ForeignKey('tag.id')),
    UniqueConstraint('corso_id', 'tag_id', name='corso_tag_unique') 
    )

class Tag(db.Model):
    id = db.Column(db.Integer(), primary_key=True)
    titolo = db.Column(db.String(255),unique=True, nullable=False)    
    
    def __init__(self, titolo):        
        self.titolo = titolo    
        
    def __repr__(self):        
        return "<Tag '{}'>".format(self.titolo)

class Corso(db.Model):
    # Nome della tabella
    __tablename__ = 'corso'
    # Struttura
    id = db.Column(db.Integer(), primary_key=True)
    titolo = db.Column(db.String(100), unique=True, nullable=False)
    descrizione = db.Column(db.String(255))
    insegnante = db.Column(db.String(100))
    livello = db.Column(db.String(50))
    # Relazione 1:n
    serate = db.relationship('Serata', backref='corso', lazy='subquery')
    # Relazione n:n
    tags = db.relationship('Tag', secondary=tags, backref=db.backref('corsi', lazy='dynamic') )
    
    # Costruttore
    def __init__(self,titolo,descrizione,insegnante,livello):
        self.titolo=titolo
        self.descrizione=descrizione
        self.insegnante=insegnante
        self.livello=livello
    
    # Print dell'oggetto
    def __repr__(self):
        return "\n{}:{} è tenuto da {}. Livello {}. Id {}. Tags {}".format(
            self.titolo,
            self.descrizione,
            self.insegnante,
            self.livello,
            self.id,
            self.tags
        )


# Tabella di relazione 1:N
class Serata(db.Model):
    __table_args__ = (UniqueConstraint('corso_id', 'descrizione', name='_corso_descrizione'),                     )
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

# LEZIONE 1
# Decoratore rotta: indirizzo pagina web
@corso.route("/corsi")
def corsi():
    lista_corsi = Corso.query.all()
    return render_template('lista.html', lista_corsi=lista_corsi, title="Corsi Python Group Biella")

# Esempio di dynamic route
@corso.route("/corsi/<int:corso_id>")
def dettaglio_corso(corso_id):
    corso = Corso.query.get_or_404(corso_id)
    serate = corso.serate
    tags = corso.tags
    if serate:
        return render_template('dettaglio_corso.html', corso=corso, sessioni=serate, title=corso.titolo)
    else:
        return render_template('corso_non_pianficato.html', corso=corso, title=corso.titolo)

# Gestore errori
@corso.errorhandler(404)
def page_not_found(error):
    return render_template('404.html'),404

if __name__ == "__main__":
    corso.run(debug=True)