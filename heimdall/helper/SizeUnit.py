from heimdall.framework.model.meta.Singleton import Singleton

class SizeUnit(metaclass=Singleton):
    
    B = {
        "factor": 0,
        "symbol": "B"
    }
    KB = {
        "factor": 1,
        "symbol": "KB"
    }
    MB = {
        "factor": 2,
        "symbol": "MB"
    }
    GB = {
        "factor": 3,
        "symbol": "GB"
    }

    def toBytes(self,value,unit):
        factor = 1024 ** unit.get('factor')
        return value * factor

    def fromBytes(self,value,unit):
        factor = 1024 ** unit.get('factor')
        return value / factor

    def convertUnit(self, value :int, from_unit, as_unit):
        bytes = self.toBytes(value,from_unit) 
        return self.fromBytes(bytes,as_unit)

    def getSymbol(self,unit):
        return unit.get('symbol')

    def fromSymbol(self,symbol):
        return getattr(SizeUnit,symbol)