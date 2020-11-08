from flask import (
    Blueprint,
    render_template,
    redirect,
    url_for,
    request,
    flash,
    session,
    current_app,
)
from project.corsi.forms import CorsiForm, write_to_disk, SerataForm
from project.models.corsi import Corso, Tag, Serata
from project import db

from sqlalchemy import desc,asc

# Define blueprint
corsi_blueprint = Blueprint("corsi", __name__, template_folder="templates")

'''
Lista dei corsi
'''
@corsi_blueprint.route("/lista", methods=["GET"])
def lista():
    # Ordinamento alfabetico ascendente per titolo
    lista_corsi = Corso.query.order_by(asc(Corso.nome)).all()
    return render_template(
        'corsi_lista.html', 
        lista_corsi=lista_corsi
    )


'''
Creazione di un corso (senza serate e senza tags)
'''
@corsi_blueprint.route("/create", methods=["GET", "POST"])
def create():

    form = CorsiForm()

    if form.validate_on_submit():

        name = form.name.data
        teacher = form.teacher.data
        level = form.level.data
        description = form.description.data

        n_course = Corso(name, teacher, level, description)
        db.session.add(n_course)

        form.name.data = ""
        form.teacher.data = ""
        form.level.data = ""
        form.description.data = ""
        
        try:
            db.session.commit()
            flash('Corso creato correttamente', 'success')
            return redirect(url_for('corsi.lista'))
        except Exception as e:
            db.session.rollback()
            flash("Errore durante la creazione del corso: %s" % str(e), 'danger')

    return render_template("corsi_create.html", form=form)


'''
Visualizzazione di un corso (con gestione serate e tags (TODO))
'''
@corsi_blueprint.route("/<int:corso_id>", methods=('GET', 'POST'))
def dettaglio_corso(corso_id):
    
    # Gestione aggiunta serate

    form = SerataForm()
    if form.validate_on_submit():

        data = form.data.data
        nome =  form.nome.data
        descrizione = form.descrizione.data
        link_partecipazione = form.link_partecipazione.data
        link_registrazione = form.link_registrazione.data

        nuova_serata = Serata(nome, descrizione, data, link_partecipazione, link_registrazione)
        nuova_serata.corso_id = corso_id
        # Reset dei campi della form
        form.data.data = ""
        form.nome.data = ""
        form.descrizione.data = ""
        form.link_partecipazione.data = ""
        form.link_registrazione.data = ""
        try:
            db.session.add(nuova_serata)
            db.session.commit()
        except Exception as e:
            flash("Errore durante l'inserimento della serata: %s" % str(e), 'error')
            db.session.rollback()
    
    corso = Corso.query.get_or_404(corso_id)
    return render_template('corsi_dettaglio.html', corso=corso, form=form)


'''
Cancellazione di un corso
'''
@corsi_blueprint.route("/delete/<int:id>", methods=('GET', 'POST'))
def corso_delete(id):
    '''
    Delete tag
    '''
    try:
        my_course = Corso.query.filter_by(id=id).first()
        db.session.delete(my_course)
        db.session.commit()
        flash('Cancellazione avvenuta con successo.', 'success')
    except Exception as e:
        db.session.rollback()
        flash("Errore durante la cancellazione del corso: %s" % str(e), 'danger')
    return redirect(url_for('corsi.lista'))

