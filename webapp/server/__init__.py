# This file tells python that server is a package

from flask import Flask
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
app.config['SECRET_KEY'] = '5791628bb0b13ce0c676dfde280ba245'
#app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///site.db' #/// => relative path from current file
#db = SQLAlchemy(app)

# must import this last because routes imports app
# i.e. "from server import app" is in routes so it needs to exist before importing
from server import routes