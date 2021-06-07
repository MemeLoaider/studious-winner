###positive_tests.py###
from test_logic.data_transfer_objects import Party, UpdateHostDTO
from test_config import party_service
import pytest


def test_get_all_parties(party_service):
    list_of_all_parties = party_service.get_all_parties()
    assert len(list_of_all_parties) >= 1, "Asserting that list is not null"


def test_create_a_party(party_service):
    party_to_create = Party(
                        party_id=None,
                        host="Tester",
                        place="Testing place",
                        number_of_ppl="100"
                      )
    response = party_service.create_party(party_to_create)
    assert response['status'] == f"party with host {party_to_create.host} has been created"


def test_change_party_host(party_service):
    # Creating party in order to change it's host
    party_to_create = Party(
                        party_id=None,
                        host="LameHost",
                        place="SupaPlace",
                        number_of_ppl="2020"
                    )
    response_from_creation = party_service.create_party(party_to_create)
    update_host_dto = UpdateHostDTO(party_id=response_from_creation['party_id'], host="SupaDupaHost!")

    response_from_updating_host = party_service.update_party_host(update_host_dto)
    assert response_from_updating_host['status'] == f"host at party_id {update_host_dto.party_id} has been updated"

