###negative_tests.py###
from test_logic.data_transfer_objects import Party, UpdateHostDTO
import random
import pytest
import random


random_invalid_data = [random.randint(199, 10000) for x in range(3)]


@pytest.mark.usefixtures("party_service", "db_session", "db_wrapper", "generator")
class TestNegative:


    @pytest.mark.parametrize("incorrect_party_id", random_invalid_data)
    def test_get_non_existent_party(db_wrapper, party_service, incorrect_party_id):  
        response = party_service.get_single_party_by_id(incorrect_party_id).json()
        assert response['status'] == "Party was not found"
    
    
    def test_update_non_existent_party_host(db_wrapper, party_service, generator):
        incorrect_request_body = UpdateHostDTO(generator.get_incorrect_party_id(), "Test Host to Mention") 
        response = party_service.update_party_host(incorrect_request_body)
        assert response['status'] == "Party was not found"



