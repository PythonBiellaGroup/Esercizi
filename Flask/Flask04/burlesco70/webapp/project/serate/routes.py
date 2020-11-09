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
from project.serate.models import Serata
from project.corsi.models import Corso
from project import db

from sqlalchemy import desc,asc

# Define blueprint
serate_blueprint = Blueprint(
    "serate", 
     __name__, 
    template_folder="templates", 
    static_folder='../static'
)    
