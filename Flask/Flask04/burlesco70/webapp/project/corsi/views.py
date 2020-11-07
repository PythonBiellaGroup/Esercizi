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
from project.corsi.forms import CorsiForm, write_to_disk, write_db, TagForm
from project.models.corsi import Corso, Tag
from project import db

from sqlalchemy import desc,asc

# from project.models.corsi import Corso
# from project import db

# Define blueprint
corsi_blueprint = Blueprint("corsi", __name__, template_folder="templates/corsi")

##Creation route
@corsi_blueprint.route("/create", methods=["GET", "POST"])
def create():

    # Get the list of serate
    # serate_list = [
    #     ("primaserata", "primaserata"),
    #     ("secondaserata", "secondaserata"),
    # ]

    # Create the form
    # form = CorsiForm(serate_list)
    form = CorsiForm()

    if form.validate_on_submit():

        course_name = form.course_name.data
        course_teacher = form.course_teacher.data
        course_lessons = form.course_lessons.data
        # course_serate = form.course_serate.data
        course_level = form.course_level.data
        course_multiple = form.course_multiple.data
        course_description = form.course_description.data

        result_list = [
            course_name,
            course_teacher,
            course_lessons,
            # course_serate,
            course_level,
            course_multiple,
            course_description,
        ]

        print("\n### CHECK RESULTS ###")
        print(course_name)
        print(result_list)
        print("#####\n")

        # Insert the result into DB
        # session["course_result"] = result_list
        course_id = write_db(
            course_name,
            course_teacher,
            course_lessons,
            course_level,
            course_description,
        )
        # course_id = course_inserted.id
        # session["course_id"] = course_inserted.id

        return redirect(url_for("corsi.results", course_id=course_id))

    return render_template("corsi_create.html", form=form)


@corsi_blueprint.route("/corsi/<int:corso_id>", methods=["GET"])
def dettaglio_corso(corso_id):
    # Gestione aggiunga serate
    '''
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
    '''
    corso = Corso.query.get_or_404(corso_id)
    return render_template('corsi_dettaglio.html', corso=corso)

##Result route
@corsi_blueprint.route("/results/<int:course_id>", methods=["GET"])
def results(course_id):

    # TODO: Use the database
    # course_list = session["course_result"]
    course = Corso.query.filter_by(id=course_id).first()
    course_list = [
        course.nome,
        course.insegnante,
        course.lezioni,
        course.livello,
        course.descrizione,
    ]
    COLUMNS = [
        "Nome corso",
        "Insegnante",
        "Lezioni",
        "Livello corso",
        "Descrizione",
    ]

    return render_template(
        "corsi_create_result.html", course_list=course_list, colnames=COLUMNS
    )

@corsi_blueprint.route("/lista", methods=["GET"])
def lista():
    # Ordinamento alfabetico ascendente per titolo
    lista_corsi = Corso.query.order_by(asc(Corso.nome)).all()
    print(lista_corsi)
    return render_template(
        'corsi_lista.html', 
        lista_corsi=lista_corsi
    )    

@corsi_blueprint.route("/tags", methods=('GET', 'POST'))
def tags():
    # Ordinamento alfabetico ascendente per titolo
    lista_tags = Tag.query.order_by(asc(Tag.name)).all()
    '''
    Crea nuovo tag
    '''
    form = TagForm()
    if form.validate_on_submit():
        tag_name = form.name.data
        n_tag = Tag(tag_name)
        print(n_tag)
        #form.populate_obj(n_tag)
        db.session.add(n_tag)
        form.name.data = ""
        try:
            db.session.commit()
            # User info
            flash('Tag creato correttamente', 'success')
            return redirect(url_for('corsi.tags'))
        except Exception as e:
            db.session.rollback()
            flash("Errore durante la creazione del tag: %s" % str(e), 'danger')

    return render_template('tags_lista.html', form=form, lista_tags=lista_tags)

@corsi_blueprint.route("/tags/delete/<int:id>", methods=('GET', 'POST'))
def tag_delete(id):
    '''
    Delete tag
    '''
    try:
        my_tag = Tag.query.filter_by(id=id).first()
        db.session.delete(my_tag)
        db.session.commit()
        flash('Cancellazione avvenuta con successo.', 'success')
    except Exception as e:
        db.session.rollback()
        flash("Errore durante la cancellazione del tag: %s" % str(e), 'danger')
    return redirect(url_for('corsi.tags'))

@corsi_blueprint.route("/tags/<id>", methods=('GET', 'POST'))
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
            flash('Aggiornamento avvenuto con successo', 'success')
        except Exception as e:
            db.session.rollback()
            flash("Errore durante l'aggiornamento del tag: %s" % str(e), 'danger')
    return render_template(
        '/tags_edit.html',
        form=form,tag=my_tag)     