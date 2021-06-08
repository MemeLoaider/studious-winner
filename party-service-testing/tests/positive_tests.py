###positive_tests.py###
from test_logic.data_transfer_objects import Party, UpdateHostDTO
from test_config import party_service, db_session, db_wrapper
import pytest


def test_get_all_parties(party_service):
    list_of_all_parties = party_service.get_all_parties()
    assert len(list_of_all_parties) >= 1, "Asserting that list is not null"
    for party in list_of_all_parties:
        assert party.__class__ is Party

def test_create_a_party(party_service, db_wrapper):
    party_to_create = Party(
                        party_id=None,
                        host="Tester",
                        place="Testing place",
                        number_of_ppl="100"
                      )
    response = party_service.create_party(party_to_create)
    assert response['status'] == "Party has been created successfully"

    # Cleaning test data
    db_wrapper.delete_party_by_id(response['party_id'])


def test_change_party_host(party_service, db_wrapper):
    # Getting the last party_id in database in order to append newly created value
    list_of_all_parties = db_wrapper.get_all_parties_from_db()
    last_used_party_id = list_of_all_parties[-1].party_id
    party_to_create = Party(
                        party_id=last_used_party_id+1,
                        host="LameHost",
                        place="SupaPlace",
                        number_of_ppl="2020"
                     )
    db_wrapper.create_party_in_db(party_to_create)

    update_host_dto = UpdateHostDTO(party_id=party_to_create.party_id, host="SupaDupaHost!")

    response_from_updating_host = party_service.update_party_host(update_host_dto)
    assert response_from_updating_host['status'] == "Party host has been updated"

    # Cleaning our test data
    db_wrapper.delete_party_by_id(party_to_create.party_id)

