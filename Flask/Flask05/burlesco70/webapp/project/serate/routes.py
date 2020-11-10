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
#from project.serate.forms import SerataForm
from project.serate.models import Serata
from project.corsi.models import Corso
from project import db

from sqlalchemy import desc,asc

from datetime import datetime

# Define blueprint
serate_blueprint = Blueprint(
    "serate", 
     __name__, 
    template_folder="templates", 
    static_folder='../static'
)

'''
Lista delle serate in ordine di data
'''
@serate_blueprint.route("/prossime", methods=["GET"])
def prossime():
    # Filtro data futura, ordinamento per data
    lista_serate = Serata.query.filter(Serata.data > datetime.now()).order_by(asc(Serata.data)).all()
    # Creo una lista parallela dei corsi collegati alle serate
    lista_corsi = [ Corso.query.filter_by(id=s.corso_id).first() for s in lista_serate ]
    # Nel template non è possibile iterare su due liste, quindi zippo le due liste e le passo
    zipped_data = zip(lista_serate, lista_corsi)
    return render_template(
        'serate_prossime.html', 
        zipped_data=zipped_data
    )

