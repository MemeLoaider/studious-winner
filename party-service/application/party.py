###party.py###
from flask import Blueprint, jsonify, request, Response
from . import db, prepare_json_response
from .models import Party


party_bp = Blueprint('party_bp', __name__)


@party_bp.route('/party', methods=['GET'])
def party():
    parties_list = [party.make_dir_from_instance() for party in Party.query.all()]
    return prepare_json_response(parties_list, 200)


@party_bp.route('/party/<int:party_id>', methods=['GET'])
def get_single_party_by_id(party_id):
    party = Party.query.filter(Party.party_id == party_id).first()
    if party is None:
        return prepare_json_response(json_body={"message": f"party with party_id {party_id} was not found"}, 
                                     status_code=404) 
    else:
        return prepare_json_response(party.make_dir_from_instance(), 200) 


@party_bp.route('/party/create', methods=['POST'])
def create_party():
    party_json = request.get_json()
    db.session.add(Party(
            host=party_json["host"],
            place=party_json["place"],
            number_of_ppl=party_json["number_of_ppl"]
        ))
    db.session.commit()
    return prepare_json_response(json_body={"status": f"party with host {party_json['host']} has been created"},
                                 status_code=201)
   

@party_bp.route('/party/update-host', methods=['PUT'])
def update_party():
    new_host_json = request.get_json()
    party_to_update = Party.query.get(new_host_json["party_id"])
    party_to_update.host = new_host_json["host"]
    db.session.commit()
    return prepare_json_response(json_body={"status": f"host at party_id {new_host_json['party_id']} has been updated"},
                                 status_code=200)

