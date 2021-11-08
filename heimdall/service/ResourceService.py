from heimdall.model.SizeUnit import SizeUnit
import psutil

from heimdall.framework.model.meta.Singleton import Singleton
from heimdall.model.Resource import Resource

class ResourceService(metaclass=Singleton):

    def getResources(self,symbol):
        unit = SizeUnit().fromSymbol(symbol)

        memory = psutil.virtual_memory()
        resource = Resource(memory,unit=unit)
        
        return resource

