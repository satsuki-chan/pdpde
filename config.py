"""
Module with app configuration for API
"""
import os
import connexion
from flask_sqlalchemy import SQLAlchemy
from flask_marshmallow import Marshmallow

basedir = os.path.abspath(os.path.dirname(__file__))
# Connexion-Application instance
conn_app = connexion.App(__name__, specification_dir=basedir)
# Flask app instance
app = conn_app.app

# Sqlite ULR for SqlAlchemy
app.config['SQLALCHEMY_ECHO'] = True   ### On Production: False
sqlite_url = "sqlite:///" + os.path.join(basedir, "db/metrobuses.db")

# Configure SqlAlchemy
app.config["SQLALCHEMY_DATABASE_URI"] = sqlite_url

# SqlAlchemy instance
db = SQLAlchemy(app)
# Initialize Marshmallow
ma = Marshmallow(app)