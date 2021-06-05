###models.py###
from . import db
from collections import OrderedDict


class Party(db.Model):
    """Data model for parties"""
    __tablename__ = "party_stuff"
    party_id = db.Column(db.Integer, primary_key=True)
    host = db.Column(db.String(50))
    place = db.Column(db.String(100))
    number_of_ppl = db.Column(db.Integer)

    def make_dir_from_instance(self):
        """Creates a propper dictionary from instance fields"""
        dictionary_to_return = self.__dict__
        del dictionary_to_return['_sa_instance_state']
        return OrderedDict(sorted(dictionary_to_return.items()))


    def __str__(self):
        return str(self.make_dir_from_instance())



