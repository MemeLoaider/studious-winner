###party.py###
from flask import Blueprint, jsonify, request, Response
from . import db


party_bp = Blueprint('party_bp', __name__)

class Party(db.Model):
    """Data model for parties"""
    __tablename__ = "party_stuff"
    party_id = db.Column(db.Integer, primary_key=True)
    host = db.Column(db.String(50))
    place = db.Column(db.String(100))
    number_of_ppl = db.Column(db.Integer)


    def __str__(self):
        dictionary_to_return = self.__dict__
        del dictionary_to_return['_sa_instance_state']
        return str(dictionary_to_return)


@party_bp.route('/party', methods=['GET'])
def party():
    return [str(party) for party in Party.query.all()]


@party_bp.route('/party/<int:party_id>', methods=['GET'])
def get_single_party_by_id(party_id):
    party = Party.query.filter(Party.party_id == party_id).first()
    response = Response(response=str(party),
                        status=200,
                        mimetype='application/json') 
    return response 

