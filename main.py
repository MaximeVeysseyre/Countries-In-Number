import json
import requests

from bson.json_util import dumps
from flask import Flask

from config.ressources import *
from config.db_access import DatabaseManager as db


app = Flask(__name__)


@app.route("/")
def hello():
    return {"welcome_message": "Hello World"}


@app.route("/api/request_country/<name>")
def route_country_by_name(name: str):

    content = json.loads(dumps(db.getInstance().get_country_by_name(name)))
    return content


@app.route("/api/add_fake/<fake_name>")
def route_fake_country(fake_name: str):

    content = json.loads(dumps(db.getInstance().add_fake_country(fake_name)))
    return content


@app.route("/api/request_density/<name>")
def route_density_slice(name: str):

    content = json.loads(dumps(db.getInstance().get_density_slice(name)))
    return content


if __name__ == "__main__":
    app.run(host='localhost', port = 8080, debug=True)