from heimdall.framework.model.meta.Singleton import Singleton
from heimdall.framework.resources.Configuraton import Configuration
from tinydb import TinyDB, Query

import inspect

class DatabaseConnection(metaclass=Singleton):

    def __init__(self) -> None:
        config = Configuration()
        self.db = TinyDB(config.database.path,sort_keys=True, indent=4)

    def getTable(self,clazz):
        if not inspect.isclass(clazz):
            raise Exception("Table exist only for class not for intance or variable")

        return self.db.table(clazz.__name__)
