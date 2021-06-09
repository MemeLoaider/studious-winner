###party.py###
from flask import Blueprint, request, current_app
from .. import db, prepare_json_response
from . import model as p


party_bp = Blueprint('party_bp', __name__)


@party_bp.route('/party', methods=['GET', 'POST'])
def party():
    if request.method == 'GET':
        current_app.logger.info("Getting request for GET ALL PARTIES")
        return p.get_all_parties()
    elif request.method == 'POST':
        current_app.logger.info(f"Getting request for CREATING A PARTY with following json: {request.get_json()}")
        return p.create_party(request.get_json())
    else:
        return prepare_json_response(json_body={"status": "incorrect request has been detected"},
                                     status_code=400)


@party_bp.route('/party/<int:party_id>', methods=['GET', 'DELETE'])
def party_with_id(party_id):
    if request.method == 'GET':
        current_app.logger.info(f"Getting a request for GETTING PARTY BY ID with following party_id: {party_id}")
        return p.get_single_party_by_id(party_id)
    elif request.method == 'DELETE':
        current_app.logger.info(f"Getting a request for DELETING PARTY BY ID with following party_id: {party_id}") 
        return p.delete_party_by_id(party_id)
    else:
        return prepare_json_response(json_body={"status": "incorrect request has been detected"},
                                     status_code=400)


@party_bp.route('/party/update-host', methods=['PUT'])
def update_party():
    current_app.logger.info(f"Getting request for CHANGING A PARTY HOST with following json: {request.get_json()}") 
    return p.update_party(request.get_json())   

