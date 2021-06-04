###party.py###
from flask import Blueprint, jsonify, request, Response
from . import db, prepare_json_response
from collections import OrderedDict


party_bp = Blueprint('party_bp', __name__)

class Party(db.Model):
    """Data model for parties"""
    __tablename__ = "party_stuff"
    party_id = db.Column(db.Integer, primary_key=True)
    host = db.Column(db.String(50))
    place = db.Column(db.String(100))
    number_of_ppl = db.Column(db.Integer)

    def make_dir_from_instance(self):
        """Creates a propper dictionary from instance fields"""
        dictionary_to_return = self.__dict__
        del dictionary_to_return['_sa_instance_state']
        return OrderedDict(sorted(dictionary_to_return.items()))


    def __str__(self):
        return str(self.make_dir_from_instance())


@party_bp.route('/party', methods=['GET'])
def party():
    return [str(party) for party in Party.query.all()]


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
   
