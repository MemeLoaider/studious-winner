###data_transfer_objects.py###

class Party:
    """Represents Party DTO"""
    def __init__(self, host, number_of_ppl, party_id, place):
        self.host = host
        self.number_of_ppl = number_of_ppl
        self.party_id = party_id
        self.place = place

    
    def __str__(self):
        return f"Party(host: {self.host}; number_of_ppl: {self.number_of_ppl}; \
party_id: {self.party_id}; place: {self.place}"

    def init_from_dictionary(dictionary: dict):
        """Instantiates a Party from dictionary"""
        return Party(
            host=dictionary['host'],
            number_of_ppl=dictionary['number_of_ppl'],
            party_id=dictionary['party_id'],
            place=dictionary['place']
        )


class UpdateHostDTO:
    """Represents DTO for updating party host"""
    def __init__(self, party_id, host):
        self.party_id = party_id
        self.host = host


    def __str__(self):
        return f"UpdateHostDTO(party_id: {self.party_id}; host: {self.host})"


