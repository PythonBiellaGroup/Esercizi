##Script to import data into DB with CRUD Operations
from project.serate.models import Serata
from project.corsi.models import Corso
from project.tags.models import Tag

from project import db
import datetime
import os

CREATE_ALL = True

#db.metadata.clear()

if CREATE_ALL:
    # Create entities
    db.create_all()
    print("Start creating structure")

    #################################################
    ####### 1. Create tags #######
    print("Start creating tags")

    t1 = Tag("Python")
    t2 = Tag("Flask")
    t3 = Tag("Pygame")
    t4 = Tag("SqlAlchemy")
    t5 = Tag("Web Development")
    t6 = Tag("Graphics")
    t7 = Tag("NumPy")
    t8 = Tag("Pandas")

    tags = [t1, t2, t3, t4, t5, t6, t7, t8]

    for t in tags:
        try:
            db.session.add(t)
            db.session.commit()
        except Exception as e:
            print(f"Eccezione: {e}")
            db.session.rollback()

    #################################################
    ##### 2. Create courses ######
    # Relazione n:n TAG - CORSO
    print("Start creating corsi")

    corsoFlask = Corso(
        "Flask",
        "Andrea Guzzo",
        "Intermedio",
        "Corso in cinque serate del microframework Flask",
    )
    corsoFlask.tags = [t1, t2, t4, t5]

    # Relazione n:n TAG - CORSO
    corsoPygame = Corso(
        "Pygame", "Mario Nardi", "Principiante", "Introduzione a Pygame"
    )
    corsoPygame.tags = [t1, t3, t6]

    corso_pandas = Corso(
        "Pandas",
        "Maria Teresa Panunzio",
        "Intermedio",
        "Corso base per manipolare i dataframes",
    )
    corso_pandas.tags = [t1, t7, t8]
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
    print("Start creating serate")

    c = Corso.query.filter_by(nome="Flask").first()  # Ritorna tutti i risultati
    s1 = Serata(
        "Flask 1",
        "Introduzione a Flask e ai web server con Jinja Base",
        datetime.date(2020, 10, 12),
    )
    s1.link_registrazione = 'https://www.youtube.com/watch?v=FPI5-oGKiVI&t=759s'
    s2 = Serata(
        "Flask 2", "Jinja avanzato e Forms", datetime.date(2020, 10, 19)
    )
    s2.link_registrazione = 'https://www.youtube.com/watch?v=C-iEkd-BpE4'
    s3 = Serata("Flask 3", "Flask con Database", datetime.date(2020, 10, 26))
    s3.link_registrazione = 'https://www.youtube.com/watch?v=rCXhuSiOcZU'
    s4 = Serata(
        "Flask 4", "Review", datetime.date(2020, 11, 2)
    )
    s4.link_registrazione = 'https://www.youtube.com/watch?v=izIKXOrbI5U'


    s5 = Serata(
        "Flask 5", "Review con Mario", datetime.date(2020, 11, 9)
    )
    
    '''TO BE DEFINED
    s6 = Serata(
        "Flask 6",
        "REST Backend e concetti avanzati",
        datetime.date(2020, 11, 9),
    )
    '''

    si6 = Serata("Da impostare", "Non ancora definita", datetime.date(2020, 11, 10))
    si7 = Serata("Da impostare", "Non ancora definita", datetime.date(2020, 11, 11))
    si8 = Serata("Da impostare", "Non ancora definita", datetime.date(2020, 11, 12))
    s1.corso_id = c.id
    s2.corso_id = c.id
    s3.corso_id = c.id
    s4.corso_id = c.id
    s5.corso_id = c.id

    serate = [s1, s2, s3, s4, s5, si6, si7, si8]
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

