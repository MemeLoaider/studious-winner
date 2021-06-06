###positive_tests.py###
from test_logic.party_service_implementation import PartyService
from test_logic.data_transfer_objects import Party
import pytest

party_service = PartyService()

def test_get_all_parties():
    list_of_all_parties = party_service.get_all_parties()
    assert len(list_of_all_parties) >= 1, "Asserting that list is not null"


def test_create_a_party():
    party_to_create = Party(
                        party_id=None,
                        host="Tester",
                        place="Testing place",
                        number_of_ppl="100"
                      )
    response = party_service.create_party(party_to_create)
    assert response['status'] == f"party with host {party_to_create.host} has been created"
