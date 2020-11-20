from app import app
import os
from controllers.names_controller import get_all_names
from flask import Response
import json


@app.route("/")
def index():
    app_name = os.environ["APP_NAME"]

    return f"Hi from {app_name}!"


@app.route("/names", methods=['GET'])
def _get_all_names():
    names = get_all_names()
    return Response(json.dumps(names), mimetype='application/json')