'''
Per eseguire:
set FLASK_APP=app.py
flask run
'''

import os
from project import create_app, db
from flask import render_template
from flask_migrate import Migrate


app = create_app('default')
# Create db and migrations
Migrate(app, db)

@app.shell_context_processor
def make_shell_context():
 return dict(db=db)

@app.route("/")
def index():
    return render_template("index.html")

'''
if __name__ == "__main__":
    app.run(debug=True)
'''
