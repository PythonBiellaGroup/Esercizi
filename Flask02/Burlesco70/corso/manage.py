from corso import corso, db, Corso

'''
Usato per dare comandi sul db usando la shell interattiva
set FLASK_APP=manage.py
flask shell
'''
@corso.shell_context_processor
def make_shell_context():  
    return dict(corso=corso, db=db, Corso=Corso) 

# Per creare il DB
# >db.create_all()