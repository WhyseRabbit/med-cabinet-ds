import pandas as pd
from flask import Flask, request

app = Flask(__name__)
app.config["DEBUG"] = True


@app.route("/", methods=["GET"])
def home():
    return "This is the beginning of the med-cabinet API."


@app.route("/strains/refresh/add_all", methods=["GET"])
def add_all():
    strain_list = pd.read_csv("../cannabis.csv")


app.run()
