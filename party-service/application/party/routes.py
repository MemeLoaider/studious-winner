###party.py###
from flask import Blueprint, request
from .. import db, prepare_json_response
from . import model as p


party_bp = Blueprint('party_bp', __name__)


@party_bp.route('/party', methods=['GET', 'POST'])
def party():
    if request.method == 'GET':
        return p.get_all_parties()
    elif request.method == 'POST':
        return p.create_party(request.get_json())
    else:
        return prepare_json_response(json_body={"status": "incorrect request has been detected"},
                                     status_code=400)


@party_bp.route('/party/<int:party_id>', methods=['GET', 'DELETE'])
def party_with_id(party_id):
    if request.method == 'GET':
        return p.get_single_party_by_id(party_id)
    elif request.method == 'DELETE':
        return p.delete_party_by_id(party_id)
    else:
        return prepare_json_response(json_body={"status": "incorrect request has been detected"},
                                     status_code=400)


@party_bp.route('/party/update-host', methods=['PUT'])
def update_party():
    return p.update_party(request.get_json())   

