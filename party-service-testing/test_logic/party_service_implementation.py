###party_service_implementation.py###
import requests
import test_config
from .data_transfer_objects import Party


class PartyService:

    base_url = test_config.PARTY_SERVICE_URL
    get_all_parties_endpoint = test_config.GET_ALL_PARTIES_ENDPOINT
    create_party_endpoint = test_config.CREATE_PARTY_ENDPOINT

    def get_all_parties(self):
        """Returns all parties from database as a list of Party objects"""
        response = requests.get(f'{self.base_url}{self.get_all_parties_endpoint}')
        return [Party.init_from_dictionary(party_json) for party_json in response.json()]


    def create_party(self, party: Party):
        """Parses given party to json and sends this data to party-service.
        As the result a new party is inserted into database.
        Returns a json response with status-message."""
        response = requests.post(f"{self.base_url}{self.create_party_endpoint}",
                                 json=party.__dict__)
        return response.json()

