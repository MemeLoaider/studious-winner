###negative_tests.py###
from test_logic.data_transfer_objects import Party, UpdateHostDTO
from test_config import party_service, db_session, db_wrapper, generator
import random
import pytest




def test_get_non_existent_party(db_wrapper, party_service, generator):  
    response = party_service.get_single_party_by_id(generator.get_incorrect_party_id()).json()
    assert response['status'] == "Party was not found"


def test_update_non_existent_party_host(db_wrapper, party_service, generator):
    incorrect_request_body = UpdateHostDTO(generator.get_incorrect_party_id(), "Test Host to Mention") 
    response = party_service.update_party_host(incorrect_request_body)
    assert response['status'] == "Party was not found"

