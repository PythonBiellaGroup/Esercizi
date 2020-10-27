from corso import corso, db, Corso, Serata, migrate

'''
Usato per dare comandi sul db usando la shell interattiva
set FLASK_APP=manage.py
flask shell
'''
@corso.shell_context_processor
def make_shell_context():  
    return dict(
        corso=corso, 
        db=db, 
        Corso=Corso,
        Serata=Serata,
        migrate=migrate) 

# Per creare il DB
# >db.create_all()
# >corsoFlask = Corso("Flask","Corso in cinque serate del microframework Flask", "Andrea Guzzo", "Intermedio")
# >corsoPygame = Corso("Pygame","Introduzione a Pygame", "Mario Nardi", "Principiante")
# >db.session.add(corsoFlask)
# >db.session.add(corsoPygame)
# >db.session.commit()
# >corsi = Corso.query.all()
'''
# Adding serate to Flask
c = Corso.query.get(1)
s1 = Serata("1 - Introduzione a Flask e ai web server con Jinja Base",datetime.date(2020, 10, 12))
s1.corso_id = c.id
db.session.add(s1)
s2 = Serata('2 - Jinja avanzato e Forms',datetime.date(2020, 10, 19))
s3 = Serata('3 - Flask con Database',datetime.date(2020, 10, 26))
s4 = Serata('4 - Large Flask Applications',datetime.date(2020, 11, 2))
s5 = Serata('5 - REST Backend e concetti avanzati',datetime.date(2020, 11, 9))
s2.corso_id = c.id
db.session.add(s2)
s3.corso_id = c.id
db.session.add(s3)
s4.corso_id = c.id
db.session.add(s4)
s5.corso_id = c.id
db.session.add(s5)
db.session.commit()
'''
