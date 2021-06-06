###model.py###
from flask import request
from .. import db, prepare_json_response
from collections import OrderedDict


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


def create_party(party_json):
    """Creates a party and inserts it into party_stuff table"""
    db.session.add(Party(
            host=party_json["host"],
            place=party_json["place"],
            number_of_ppl=party_json["number_of_ppl"]
        ))
    db.session.commit()
    # Searching for newly created party by given params
    newly_created_party = Party.query.filter(Party.host == party_json['host'] 
                                             and Party.place == party_json['place'] 
                                             and Party.number_of_ppl == party_json['number_of_ppl']).order_by(Party.party_id.desc()).first()
    return prepare_json_response(json_body={
                                            "status": f"party with host {party_json['host']} has been created",
                                            "party_id": f"{newly_created_party.party_id}"
                                           },
                                 status_code=201)   


def delete_party_by_id(party_id):
    """Deletes party with given <party_id> from the party_stuff table"""
    Party.query.filter(Party.party_id == party_id).delete()
    db.session.commit()
    return prepare_json_response(json_body={"status": f"party with party_id = {party_id} has been deleted"},
                                 status_code=200)

