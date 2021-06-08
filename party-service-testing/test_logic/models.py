###models.py###
from .data_transfer_objects import Party

class PartyStuffWrapper:
    """Wraps party_stuff session and performs actions with DB"""
    def __init__(self, db_session):
        self.db_session = db_session


    def get_all_parties_from_db(self):
        """Returns a list of all parties"""
        return self.db_session.query(Party)


    def get_party_by_id_from_db(self, party_id):
        """Returns a party from DB by given <party_id>"""
        return self.db_session.query(Party).filter(Party.party_id == party_id).first()
    

    def create_party_in_db(self, party: Party):
        """Creates a party in DB""" 
        self.db_session.add(party) 
        self.db_session.commit()

    
    def delete_party_by_id(self, party_id):
        """Deletes a party from DB by given <party_id>"""
        party_to_delete = self.get_party_by_id_from_db(party_id)
        self.db_session.delete(party_to_delete)
        self.db_session.commit()

    
