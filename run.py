import os
import json
from flask import Flask, render_template


app = Flask(__name__)


#  Decorator starts with @ to wrap functions
#  app.route() function binds a file to the 'view' of the file with that name
#  Flask command 'render_template' looks in 'templates' folder for the file passed to the function
@app.route("/")
def index():
    return render_template("index.html", page_title="Home")


@app.route("/about")
def about():
    data = []
    with open("data/company.json", "r") as json_data:
        data = json.load(json_data)
    return render_template("about.html", page_title="About", company=data)


@app.route("/contact")
def contact():
    return render_template("contact.html", page_title="Contact")


@app.route("/careers")
def careers():
    return render_template("careers.html", page_title="Careers")


if __name__ == "__main__":
    app.run(
        host=os.environ.get("IP", "0.0.0.0"),
        port=int(os.environ.get("PORT", "5000")),
        debug=True)
        # MUST NOT HAVE debug=True in submitted project!!!
        # Only to be used in developmental testing stage. Change to debug=False before submitting
     