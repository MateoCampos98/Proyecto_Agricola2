"""
import uuid

class Client:

    def __init__(self, name, company, email, position, uid=None):
        self.name = name
        self.company = company
        self.email = email
        self.position = position
        self.uid = uid or uuid.uuid4()

    def to_dict(self):
        return vars(self)
    
    @staticmethod
    def schema():
        return["name", "company", "email", "position", "uid"]

"""
from common.models import PVClient


class Client(PVClient):

    def __init__(self, name, company, email, position, uid=None):
        super().__init__(uid)
        self.name = name
        self.company = company
        self.email = email
        self.position = position

    @staticmethod
    def schema():
        return ['name', 'company', 'email', 'position', 'uid']