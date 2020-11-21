
from flask import Blueprint, render_template
from project.ruoli.models import Permission

main_blueprint = Blueprint(
    "main",
    __name__, 
    template_folder="templates",
    static_folder='../static'
)

@main_blueprint.app_context_processor
def inject_permissions():
    return dict(Permission=Permission)

@main_blueprint.route("/", methods=['GET', 'POST'])
def index():
    return render_template("index.html")