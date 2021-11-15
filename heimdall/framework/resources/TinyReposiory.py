import json
from tinydb import Query

class TinyRepository:

    def __init__(self) -> None:
        self.clazz = None

    def jsonify(self,obj):
        return json.loads(json.dumps(obj,default=lambda o: o.__dict__))

    def assertType(self,obj):
        if type(obj) != self.clazz:
            raise Exception("Object is not of type {}" + self.clazz.__name__)