'''
Per eseguire:

set FLASK_APP=app.py
flask run

oppure

python app.py

Per cambiare configurazione da ambiente:
set FLASK_CONFIG=...

'''

import os
from project import create_app, db
from flask import render_template
from flask_migrate import Migrate


app = create_app(os.getenv('FLASK_CONFIG') or 'default')
# Create db and migrations
Migrate(app, db)

@app.shell_context_processor
def make_shell_context():
 return dict(db=db)

'''
Per i test di unità automatici
The app.cli.command decorator makes it simple to implement custom commands.
The name of the decorated function is used as the command name, and the function’s
docstring is displayed in the help messages. The implementation of the test() func‐
tion invokes the test runner from the unittest package.

Per testare:

set FLASK_APP=app.py
flask test

'''
@app.cli.command()
def test():
 """Run the unit tests."""
 import unittest
 tests = unittest.TestLoader().discover('tests')
 unittest.TextTestRunner(verbosity=2).run(tests)

@app.route("/")
def index():
    return render_template("index.html")

if __name__ == "__main__":
    app.run(debug=True)
