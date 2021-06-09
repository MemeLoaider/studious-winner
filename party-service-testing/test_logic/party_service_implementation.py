###party_service_implementation.py###
import requests
from .utils import log_request_and_response
from .data_transfer_objects import Party, UpdateHostDTO


class PartyService:


    def __init__(self, endpoints: dict):
        self.base_url = endpoints['base_url']
        self.get_all_parties_endpoint = endpoints['get_all_parties_endpoint']
        self.create_party_endpoint = endpoints['create_party_endpoint']
        self.update_party_host_endpoint = endpoints['update_party_host_endpoint']
        self.delete_party_by_id_endpoint = endpoints["delete_party_by_id_endpoint"]
        self.dictionary = endpoints 


    @log_request_and_response(request_method="GET", endpoint="get_all_parties_endpoint")
    def get_all_parties(self):
        """Returns all parties from database as a list of Party objects"""
        response = requests.get(f"{self.base_url}{self.get_all_parties_endpoint}")
        return [Party.init_from_dictionary(party_json) for party_json in response.json()]


    @log_request_and_response(request_method="POST", endpoint="create_party_endpoint")
    def create_party(self, party: Party):
        """Parses given party to json and sends this data to party-service.
        As the result a new party is inserted into database.
        Returns a json response with status-message."""
        response = requests.post(f"{self.base_url}{self.create_party_endpoint}",
                                 json=party.as_json())
        return response.json()

    
    @log_request_and_response(request_method="PUT", endpoint="update_party_host_endpoint")
    def update_party_host(self, host_to_update: UpdateHostDTO):
        """Parses given <host_to_update> DTO into json and sends this data.
        As the result host is being updated in DB.
        Returns a json response"""
        response = requests.put(url=f"{self.base_url}{self.update_party_host_endpoint}",
                                json=host_to_update.__dict__)
        return response.json()

    
    @log_request_and_response(request_method="DELETE", endpoint="delete_party_by_id_endpoint")
    def delete_party_by_id(self, party_id):
        """Deletes party by given <party_id>.
        Returns a json response"""
        return requests.delete(url=f"{self.base_url}{self.delete_party_by_id_endpoint}{party_id}").json() 

