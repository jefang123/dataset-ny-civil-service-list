from flask import Blueprint, jsonify, make_response

errors = Blueprint('errors', __name__)

BAD_REQ = 'bad requrest'
NOT_FOUND = 'not found'

@errors.app_errorhandler(400)
def bad_request(error):
    return make_response(jsonify({'error': BAD_REQ}), 400)

@errors.app_errorhandler(404)
def not_found(error):
    return make_response(jsonify({'error': NOT_FOUND}), 404)
