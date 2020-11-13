## Script to import data into DB with CRUD Operations
from project.serate.models import Serata
from project.corsi.models import Corso
from project.tags.models import Tag

from project import db,create_app
import datetime
import os

CREATE_ALL = True

if CREATE_ALL:
    # Utilizzo dell'application factory
    app = create_app(os.getenv('FLASK_CONFIG') or 'default')
    app_context = app.app_context()
    app_context.push()
    
    db.create_all()

    print("Start creating structure")
    # Create entities
    #################################################
    ####### 1. Create tags #######
    print("Start creating tags")
    Tag.insert_default_tags()

    #################################################
    ##### 2. Create courses ######
    # Relazione n:n TAG - CORSO
    print("Start creating corsi")

    corsoFlask = Corso(
        "Flask",
        "Andrea Guzzo",
        "Intermedio",
        "Corso in cinque serate del microframework Flask",
        "flask-icon.png"
    )
    corsoFlask.tags = [
        Tag.query.filter_by(name="Python").first(), 
        Tag.query.filter_by(name="Flask").first(), 
        Tag.query.filter_by(name="Web Development").first(), 
        Tag.query.filter_by(name="SqlAlchemy").first()
        ]

    # Relazione n:n TAG - CORSO
    corsoPygame = Corso(
        "Pygame", "Mario Nardi", "Principiante", "Introduzione a Pygame", "pygame-icon.png"
    )
    corsoPygame.tags = [
        Tag.query.filter_by(name="Python").first(), 
        Tag.query.filter_by(name="Pygame").first(), 
        Tag.query.filter_by(name="Graphics").first()]

    corso_pandas = Corso(
        "Pandas",
        "Maria Teresa Panunzio",
        "Intermedio",
        "Corso base per manipolare i dataframes",
    )
    corso_pandas.tags = [
        Tag.query.filter_by(name="Python").first(), 
        Tag.query.filter_by(name="Pandas").first(), 
        Tag.query.filter_by(name="NumPy").first()]
    corsi = [corsoFlask, corsoPygame, corso_pandas]

    for c in corsi:
        try:
            db.session.add(c)
            db.session.commit()
        except Exception as e:
            print(f"Eccezione: {e}")
            db.session.rollback()

    #################################################
    ##### 3. Create Serate ######
    # Creo e riutilizzerò l'oggetto data_serata
    data_serata = datetime.datetime(2020, 10, 12)
    data_serata = data_serata.replace(hour=20)
    
    print("Start creating serate")

    c = Corso.query.filter_by(nome="Flask").first()  # Ritorna tutti i risultati
    s1 = Serata(
        "Flask 1",
        "Introduzione a Flask e ai web server con Jinja Base",
        data_serata,
    )
    data_serata = data_serata.replace(day=19)
    s1.link_registrazione = 'https://www.youtube.com/watch?v=FPI5-oGKiVI&t=759s'
    s2 = Serata(
        "Flask 2", "Jinja avanzato e Forms", data_serata
    )
    data_serata = data_serata.replace(day=26)
    s2.link_registrazione = 'https://www.youtube.com/watch?v=C-iEkd-BpE4'
    s3 = Serata("Flask 3", "Flask con Database", data_serata)
    s3.link_registrazione = 'https://www.youtube.com/watch?v=rCXhuSiOcZU'
    data_serata = data_serata.replace(day=2, month=11)
    s4 = Serata(
        "Flask 4", "Review", data_serata
    )
    s4.link_registrazione = 'https://www.youtube.com/watch?v=izIKXOrbI5U'

    data_serata = data_serata.replace(day=9, month=11)
    s5 = Serata(
        "Flask 5", "Review con Mario", data_serata
    )

    data_serata = data_serata.replace(day=16)
    s6 = Serata(
        "Flask 6", "Review con altri esercizi", data_serata
    )

    data_serata = data_serata.replace(day=23)
    s7 = Serata(
        "Flask 7", "REST Backend e concetti avanzati", data_serata
    )
    s1.corso_id = c.id
    s2.corso_id = c.id
    s3.corso_id = c.id
    s4.corso_id = c.id
    s5.corso_id = c.id
    s6.corso_id = c.id
    s7.corso_id = c.id

    data_serata = data_serata.replace(day=30)
    si6 = Serata("Da impostare", "Non ancora definita", data_serata)

    serate = [s1, s2, s3, s4, s5, s6, s7, si6]
    for s in serate:
        try:
            db.session.add(s)
            db.session.commit()
        except Exception as e:
            print(f"Eccezione: {e}")
            db.session.rollback()


#################################################
###DEBUGS
print("\n#### DATA DEBUG ####\n")

# Read a course
courses = Corso.query.all()
print(f"\nList of all courses: {courses}")

# Get a course by name
c = Corso.query.filter_by(nome="Flask").first()  # Ritorna il corso di Flask
print(f"\nFlask course: {c}")

# Get all serate
list_serate = Serata.query.all()
print(f"\nSerate create:")
for serata in list_serate:
    print(f"Serata: {serata.id}, {serata.nome}, in data: {serata.data}")

# Get a serate by serate name
list_impostare = Serata.query.filter(Serata.nome.like("%impostare%")).all()
print(f"\nSerate da impostare:")
for i in list_impostare:
    print(f"Serate ancora da impostare: {i.id}, {i.nome}, in data: {i.data}")

db.session.remove()