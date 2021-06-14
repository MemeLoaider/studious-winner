###negative_tests.py###
from test_logic.data_transfer_objects import Party, UpdateHostDTO
from test_config import party_service, db_session, db_wrapper
import random
import pytest


def test_get_non_existent_party(db_wrapper, party_service):
    # Getting all valid party_ids in order to set invalid one
    list_of_party_ids = []
    for party in db_wrapper.get_all_parties_from_db():
        list_of_party_ids.append(party.party_id)

    incorrect_party_id = None
    while True:
        incorrect_party_id = random.randint(list_of_party_ids[-1], 1000)
        if incorrect_party_id not in list_of_party_ids:
            break

    response = party_service.get_single_party_by_id(incorrect_party_id).json()
    assert response['status'] == "Party was not found"

