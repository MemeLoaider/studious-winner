###party.py###
from flask import Blueprint, jsonify, request, Response
from . import db, prepare_json_response
from .models import Party


party_bp = Blueprint('party_bp', __name__)


@party_bp.route('/party', methods=['GET', 'POST'])
def party():
    if request.method == 'GET':
        return get_all_parties()
    elif request.method == 'POST':
        return create_party()
    else:
        return prepare_json_response(json_body={"status": "incorrect request has been detected"},
                                     status_code=400)

@party_bp.route('/party/<int:party_id>', methods=['GET', 'DELETE'])
def party_with_id(party_id):
    if request.method == 'GET':
        return get_single_party_by_id(party_id)
    elif request.method == 'DELETE':
        return delete_party_by_id(party_id)
    else:
        return prepare_json_response(json_body={"status": "incorrect request has been detected"},
                                     status_code=400)


@party_bp.route('/party/update-host', methods=['PUT'])
def update_party():
    """Updates party host at given <party_id> in json"""
    new_host_json = request.get_json()
    party_to_update = Party.query.get(new_host_json["party_id"])
    party_to_update.host = new_host_json["host"]
    db.session.commit()
    return prepare_json_response(json_body={"status": f"host at party_id {new_host_json['party_id']} has been updated"},
                                 status_code=200)

   
def get_single_party_by_id(party_id):
    """Returns single party by <party_id> from party_stuff table"""
    party = Party.query.filter(Party.party_id == party_id).first()
    if party is None:
        return prepare_json_response(json_body={"message": f"party with party_id {party_id} was not found"}, 
                                     status_code=404) 
    else:
        return prepare_json_response(party.make_dir_from_instance(), 200) 


def get_all_parties():
    """Returns all parties from party_stuff table"""
    parties_list = [party.make_dir_from_instance() for party in Party.query.all()]
    return prepare_json_response(parties_list, 200)


def create_party():
    """Creates a party and inserts it into party_stuff table"""
    party_json = request.get_json()
    db.session.add(Party(
            host=party_json["host"],
            place=party_json["place"],
            number_of_ppl=party_json["number_of_ppl"]
        ))
    db.session.commit()
    return prepare_json_response(json_body={"status": f"party with host {party_json['host']} has been created"},
                                 status_code=201)   


def delete_party_by_id(party_id):
    """Deletes party with given <party_id> from the party_stuff table"""
    Party.query.filter(Party.party_id == party_id).delete()
    db.session.commit()
    return prepare_json_response(json_body={"status": f"party with party_id = {party_id} has been deleted"},
                                 status_code=200)

