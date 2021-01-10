import pandas as pd
from flask import Flask, request
from flask_sqlalchemy import SQLAlchemy

"""Creating Flask app instance, complete with SQLAlchemy database."""
app = Flask(__name__)
app.config["DEBUG"] = True
app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:////tmp/strains.db"
DB = SQLAlchemy(app)


"""Creating database for Strains information."""
class Strains(DB.Model):
    id = DB.Column(DB.Integer, primary_key=True)
    strain = DB.Column(DB.String(10), unique=True, nullable=False)
    bud_type = DB.Column(DB.String(5), unique=False, nullable=False)
    rating = DB.Column(DB.Float, unique=False, nullable=False)
    effects = DB.Column(DB.Text, unique=True, nullable=True)
    flavor = DB.Column(DB.Text, unique=True, nullable=True)
    description = DB.Column(DB.Text, unique=True, nullable=True)

def __repr__(self):
    return "<User %r>" % self.strain


"""This route takes user to the landing page."""
@app.route("/", methods=["GET"])
def home():
    return "This is the beginning of the med-cabinet API."


"""This resets and updates database."""
@app.route("/strains/refresh/add_all", methods=["GET"])
def add_all():
    DB.drop_all()
    DB.create_all()


app.run()
