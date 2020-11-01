from flask import Flask, render_template, request, session, url_for, redirect, flash
# Forms
from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField, BooleanField, RadioField, SelectField, TextAreaField, DateField, SelectMultipleField
from wtforms.validators import DataRequired, Length
# Model
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy.schema import UniqueConstraint
from sqlalchemy import desc,asc
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

# MODELLO
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
    
    '''
    def __init__(self, titolo):        
        self.titolo = titolo    
    '''
        
    def __repr__(self):        
        return "<Tag '{}'>".format(self.titolo)

class Corso(db.Model):
    # Nome della tabella
    __tablename__ = 'corso'
    # Struttura/Attributi
    id = db.Column(db.Integer(), primary_key=True)
    titolo = db.Column(db.String(100), unique=True, nullable=False)
    descrizione = db.Column(db.String(255))
    insegnante = db.Column(db.String(100))
    livello = db.Column(db.String(50))
    # Relazione 1:n; ordinamento serate per data
    serate = db.relationship('Serata', order_by="asc(Serata.data)", backref='corso', lazy='subquery')
    # Relazione n:n
    tags = db.relationship('Tag', secondary=tags, backref=db.backref('corsi', lazy='dynamic') )
    
    # Costruttore
    '''
    NOTA: Lasciare il costruttore crea problemi nella gestione della form di creazione
    def __init__(self,titolo,descrizione,insegnante,livello):
        self.titolo=titolo
        self.descrizione=descrizione
        self.insegnante=insegnante
        self.livello=livello
    '''
    
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

    '''
    def __init__(self, descrizione, data):
        self.descrizione = descrizione
        self.data = data
    '''

    def __repr__(self):
        return "<Descrizione '{}'>".format(self.descrizione)
# FINE MODELLO

def index():
    user_agent = request.headers.get('User-Agent')
    return render_template('index.html', user_agent=user_agent)
# Altro modo per fare routing
# add_url_rule: the URL, the endpoint name, and the view function
corso.add_url_rule('/', 'index', index)

'''
Semplice form per la creazione di un nuovo TAG slegato da qualsiasi corso
'''
class TagForm(FlaskForm):
    titolo = StringField(u'Titolo tag', validators=[Length(min=-1, max=255, message='Massimo 255 caratteri')])

# Gestione tags
@corso.route("/tags", methods=('GET', 'POST'))
def tags():
    # Ordinamento alfabetico ascendente per titolo
    lista_tags = Tag.query.order_by(asc(Tag.titolo)).all()
    '''
    Crea nuovo tag
    '''
    form = TagForm()
    if form.validate_on_submit():
        n_tag = Tag()
        form.populate_obj(n_tag)
        db.session.add(n_tag)
        form.titolo.data = ""
        try:
            db.session.commit()
            # User info
            flash('Tag creato correttamente', 'success')
            return redirect(url_for('tags'))
        except Exception as e:
            db.session.rollback()
            flash("Errore durante la creazione del tag: %s" % str(e), 'danger')

    return render_template('nuovo_tag.html', form=form, lista_tags=lista_tags)

@corso.route("/tags/delete", methods=('POST',))
def tag_delete():
    '''
    Delete tag
    '''
    try:
        my_tag = Tag.query.filter_by(id=request.form['id']).first()
        db.session.delete(my_tag)
        db.session.commit()
        flash('Cencellazione avvenuta con successo.', 'success')
    except Exception as e:
        db.session.rollback()
        flash("Errore durante la cancellazione del tag: %s" % str(e), 'danger')
    return redirect(url_for('tags'))

@corso.route("/edit_tag/<id>", methods=('GET', 'POST'))
def edit_tag(id):
    '''
    Edit tag
    :param id: Id from tag
    '''
    my_tag = Tag.query.filter_by(id=id).first()
    form = TagForm(obj=my_tag)
    if form.validate_on_submit():
        try:
            # Update tag
            form.populate_obj(my_tag)
            db.session.add(my_tag)
            db.session.commit()
            # User info
            flash('Aggiornamento avventuo con successo', 'success')
        except Exception as e:
            db.session.rollback()
            flash("Errore durante l'aggiornamento del tag: %s" % str(e), 'danger')
    return render_template(
        '/edit_tag.html',
        form=form)      

# Lista corsi
# Decoratore rotta: indirizzo pagina web
@corso.route("/corsi")
def corsi():
    # Ordinamento alfabetico ascendente per titolo
    lista_corsi = Corso.query.order_by(asc(Corso.titolo)).all()
    return render_template('lista.html', lista_corsi=lista_corsi, title="Corsi Python Group Biella")

class SerataForm(FlaskForm):
    data = DateField(u'Data', format='%d/%m/%Y',id='datepick')
    descrizione = StringField(u'Descrizione', validators=[Length(min=-1, max=255, message='Massimo 255 caratteri')])

# Esempio di dynamic route
# Esempio di inserimento "entità figlio": inserire una serata
@corso.route("/corsi/<int:corso_id>", methods=('GET', 'POST'))
def dettaglio_corso(corso_id):
    # Gestione aggiunga serate
    form = SerataForm()
    if form.validate_on_submit():
        nuova_serata=Serata()
        nuova_serata.data = form.data.data 
        nuova_serata.descrizione = form.descrizione.data
        nuova_serata.corso_id = corso_id
        # Reset
        form.data.data = ""
        form.descrizione.data = ""
        try:
            db.session.add(nuova_serata)
            db.session.commit()
        except Exception as e:
            flash("Errore durante l'inserimento della serata: %s" % str(e), 'error')
            db.session.rollback()

    corso = Corso.query.get_or_404(corso_id)
    serate = corso.serate
    tags = corso.tags
    return render_template('dettaglio_corso.html', form=form, corso=corso, sessioni=serate, title=corso.titolo)
    '''
    if serate:
        return render_template('dettaglio_corso.html', form=form, corso=corso, sessioni=serate, title=corso.titolo)
    else:
        return render_template('corso_non_pianficato.html', corso=corso, title=corso.titolo)
    '''

class CorsoForm(FlaskForm):
    titolo = StringField(u'Titolo del corso', validators=[DataRequired(), Length(min=-1, max=100, message='Massimo 100 caratteri')])
    descrizione = StringField(u'Descrizione', validators=[Length(min=-1, max=255, message='Massimo 255 caratteri')])
    insegnante = StringField(u'Insegnante', validators=[Length(min=-1, max=100, message='Massimo 100 caratteri')])
    livello = SelectField(u'Livello', choices=[('Facile', 'Facile'), ('Intermedio', 'Intermedio'), ('Difficile', 'Difficile')])
    tag = SelectMultipleField(u'Tags', coerce=int)

# Nuovo corso
@corso.route("/nuovo_corso", methods=('GET', 'POST'))
def nuovo_corso():
    '''
    Crea nuovo corso
    '''
    form = CorsoForm()
    tags = [(t.id, t.titolo) for t in Tag.query.all()]  
    form.tag.choices = tags
    if form.validate_on_submit():
        n_corso = Corso()
        form.populate_obj(n_corso)
        #n_corso.tags = form.tag.data -> errore
        #n_corso.tags = request.form.getlist('tag') -> errore
        db.session.add(n_corso)
        try:
            db.session.commit()
            # User info
            flash('Corso creato correttamente', 'success')
            return redirect(url_for('corsi'))
        except:
            db.session.rollback()
            flash('Errore durante la creazione del corso.', 'danger')

    return render_template('nuovo_corso.html', form=form)

# Edit non funziona
@corso.route("/edit_corso/<id>", methods=('GET', 'POST'))
def edit_corso(id):
    # Lista dei tag disponibili
    available_tags = Tag.query.all()
    tag_list = [(t.id, t.titolo) for t in available_tags]

    my_corso = Corso.query.filter_by(id=id).first()
    form = CorsoForm(obj=my_corso)
    # Tutti i tag come tupla (id, titolo)
    form.tag.choices = tag_list

    if form.validate_on_submit():
        try:
            # Update corso
            form.populate_obj(my_corso)
            ###########################
            # Non capisco come riportare qui le selezioni dei tag
            ###########################
            tag_choices = form.tag.choices
            print(tag_choices)
            # my_corso.tags = [id for (i,_) in tag_choices]
            db.session.add(my_corso)
            db.session.commit()
            # info
            flash('Aggiornamento avvenuto con successo', 'success')
        except Exception as e:
            db.session.rollback()            
            flash("Errore durante l'inserimento della serata: %s" % str(e), 'error')
    return render_template(
        'edit_corso.html',
        form=form)          

# Gestore errori
@corso.errorhandler(404)
def page_not_found(error):
    return render_template('404.html'),404

if __name__ == "__main__":
    corso.run(debug=True)