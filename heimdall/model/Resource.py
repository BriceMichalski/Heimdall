from heimdall.framework.model.ApiResource import ApiResource

from heimdall.model.SizeUnit import SizeUnit

class Resource(ApiResource):

    def __init__(self,memory,cpu =None,disk =None, unit=SizeUnit.B) -> None:
        sizeUnit = SizeUnit()

        self.unit = sizeUnit.getSymbol(unit)
        self.memory = {
            "total" : sizeUnit.fromBytes(memory.total,unit),
            "available" : sizeUnit.fromBytes(memory.available,unit),
            "used" : sizeUnit.fromBytes(memory.used,unit),
            "free" : sizeUnit.fromBytes(memory.free,unit)
        }
        self.cpu = cpu
        self.disk = disk
