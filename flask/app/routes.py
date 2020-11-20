from app import app
import os
from controllers.names_controller import get_all_names, add_names
from flask import Response, request
import json


@app.route("/")
def index():
    app_name = os.environ["APP_NAME"]

    return f"Hi from {app_name}!!! Hej hej!!!"


@app.route("/names", methods=['GET'])
def _get_all_names():
    names = get_all_names()
    return Response(json.dumps(names), mimetype='application/json')


@app.route("/names", methods=["POST"])
def _post_names():
    data = request.get_json()
    add_names(data)
    return json.dumps({'success': True}), 200, {'ContentType': 'application/json'}
