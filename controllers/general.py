from flask import Blueprint, send_from_directory, jsonify
import os

general_blueprint = Blueprint('general', __name__)

@general_blueprint.route('/', methods=['GET'])
def serve_index():
    return send_from_directory('static', 'index.html')

@general_blueprint.route('/getapi', methods=['GET'])
def get_string():
    return jsonify({"message": "This is a simple string response."})
