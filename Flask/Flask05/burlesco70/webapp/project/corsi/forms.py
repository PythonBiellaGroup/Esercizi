from time import strftime
from flask_wtf import FlaskForm
# from project.models.corsi import Serata
# from project.corsi.models import Corso
from wtforms import (
    Form,
    validators,
    StringField,
    IntegerField,
    SubmitField,
    BooleanField,
    SelectField,
    TextAreaField,
    DateField
)
from wtforms.validators import DataRequired, Length

'''
Corso Form
'''
class CorsiForm(FlaskForm):

    course_level_list = [
        ("principiante", "Principiante"),
        ("facile", "Facile"),
        ("medio", "Medio"),
        ("avanzato", "Avanzato"),
        ("esperto", "Esperto"),
    ]

    # String field: Name of the course
    name = StringField(
        "Name of the course",
        validators=[
            validators.Length(min=1, max=120),
            validators.required("Inserisci il nome del corso"),
        ],
    )
    # String field: Course Teacher
    teacher = StringField(
        "Teacher",
        validators=[
            validators.Length(min=1, max=120),
            validators.required("Inserisci il nome dell'insegnante"),
        ],
    )

    # Livello di difficoltà del corso
    level = SelectField(
        "Livello del corso",
        choices=course_level_list,
        validators=[
            validators.required("Definisci il livello di difficoltà del corso")
        ],
    )

    # Free Text: Descrizione del corso
    description = TextAreaField("Descrizione del corso")

    # Submit button
    submit = SubmitField("Crea nuovo corso")


# Utilities functions
def get_time():
    time = strftime("%Y-%m-%dT%H:%M")
    return time


def write_to_disk(name, surname, email):
    data = open("file.log", "a")
    timestamp = get_time()
    data.write(
        "DateStamp={}, Name={}, Surname={}, Email={} \n".format(
            timestamp, name, surname, email
        )
    )
    data.close()


'''
Serata Form
'''
class SerataForm(FlaskForm):
    nome = StringField(
        u'Titolo della serata', 
        validators=[Length(min=-1, max=100, message='Massimo 100 caratteri')]
    )
    descrizione = StringField(
        u'Descrizione', 
        validators=[Length(min=-1, max=255, message='Massimo 255 caratteri')]
    )
    data = DateField(u'Data', format='%d/%m/%Y',id='datepick')
    link_partecipazione = StringField(
        u"Link di partecipazione all'incontro",
        validators=[Length(min=-1, max=255, message='Massimo 255 caratteri')]
    )
    link_registrazione = StringField(
        u"Link della registrazione dell'incontro",
        validators=[Length(min=-1, max=255, message='Massimo 255 caratteri')]
    )


