from flask import Flask

app = Flask(__name__)
app.config["DEBUG"] = True


@app.route("/", methods=["GET"])
def home():
    return "This is the beginning of the med-cabinet API."


app.run()
