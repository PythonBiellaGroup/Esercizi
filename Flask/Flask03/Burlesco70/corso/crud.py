import datetime
from corso import db, Corso, Serata, Tag

db.create_all()

t1 = Tag('Python')
t2 = Tag('Flask')
t3 = Tag('Pygame')
t4 = Tag('SqlAlchemy')
t5 = Tag('Web Development')
t6 = Tag('Graphics')
tags = [t1,t2,t3,t4,t5,t6]

for t in tags:
    try:
        db.session.add(t)
        db.session.commit()
    except Exception as e:
        print(f"Eccezione: {e}")
        db.session.rollback()


corsoFlask = Corso("Flask","Corso in cinque serate del microframework Flask", "Andrea Guzzo", "Intermedio")
# Relazione n:n TAG - CORSO
corsoFlask.tags = [t1,t2,t4,t5]
corsoPygame = Corso("Pygame","Introduzione a Pygame", "Mario Nardi", "Principiante")
# Relazione n:n TAG - CORSO
corsoPygame.tags = [t1,t3,t6]    

corso_pandas = Corso("Pandas","Corso base per manipolare i dataframes", "Maria Teresa", "Intermedio")
# db.session.add_all([corsoFlask, corsoPygame])
corsi = [corsoFlask, corsoPygame, corso_pandas]
for c in corsi:
    try:
        db.session.add(c)
        db.session.commit()
    except Exception as e:
        print(f"Eccezione: {e}")
        db.session.rollback()

# READ / SELECT
# Read all
tutti = Corso.query.all()
print(tutti)
# Per Id
corso_sel = Corso.query.get(3)
print(corso_sel)
# Per filtro
corso_sel = Corso.query.filter_by(titolo='Flask') #Ritorna tutti i risultati
print(corso_sel.all()) #Lista
print(corso_sel.first()) #Il primo

# UPDATE
corso_flask = Corso.query.filter_by(titolo='Flask').first()
if corso_flask.livello == "Difficile":
    corso_flask.livello = "Intermedio"
else:
    corso_flask.livello = "Difficile"
db.session.add(corso_flask)
db.session.commit()
corso_flask = Corso.query.filter_by(titolo='Flask').first()
print(corso_flask)


# DELETE
corso_pandas = Corso.query.filter_by(titolo='Pandas').first()
try:
    db.session.delete(corso_pandas)
    db.session.commit()
except Exception as e:
    print(f"Eccezione: {e}")
    db.session.rollback()

# Relazione 1:n CORSO -> SERATA

c = Corso.query.filter_by(titolo='Flask').first() #Ritorna tutti i risultati
s1 = Serata("1 - Introduzione a Flask e ai web server con Jinja Base",datetime.date(2020, 10, 12))
s2 = Serata('2 - Jinja avanzato e Forms',datetime.date(2020, 10, 19))
s3 = Serata('3 - Flask con Database',datetime.date(2020, 10, 26))
s4 = Serata('4 - Large Flask Applications',datetime.date(2020, 11, 2))
s5 = Serata('5 - REST Backend e concetti avanzati',datetime.date(2020, 11, 9))
s1.corso_id = c.id
s2.corso_id = c.id
s3.corso_id = c.id
s4.corso_id = c.id
s5.corso_id = c.id

serate = [s1, s2, s3, s4, s5]
for s in serate:
    try:
        db.session.add(s)
        db.session.commit()
    except Exception as e:
        print(f"Eccezione: {e}")
        db.session.rollback()