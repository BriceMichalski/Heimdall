from heimdall.helper.SizeUnit import SizeUnit
import psutil

from heimdall.framework.model.meta.Singleton import Singleton
from heimdall.model.Resource import Resource

class ResourceService(metaclass=Singleton):

    def __init__(self) -> None:
        self.unitHelper = SizeUnit()

    def getResources(self,symbol):
        unit = self.unitHelper.fromSymbol(symbol)

        memory = psutil.virtual_memory()
        
        cpuPercent  = psutil.cpu_percent()
        cpuPercentDetail :list = psutil.cpu_percent(percpu=True)
        cpuPercentTargetting = {key+1: value for (key,value) in enumerate(cpuPercentDetail)}

        disk = {}
        for partition in psutil.disk_partitions():
            if not partition.mountpoint.startswith('/snap'):
                disk_usage = psutil.disk_usage(partition.mountpoint)
                disk[partition.mountpoint] = {
                    "total": self.unitHelper.fromBytes(disk_usage.total,unit),
                    "used": self.unitHelper.fromBytes(disk_usage.used,unit),
                    "free": self.unitHelper.fromBytes(disk_usage.free,unit),
                    "percent": self.unitHelper.fromBytes(disk_usage.percent,unit)
                }

        cpu = {
            "count": psutil.cpu_count(),
            "usage_percentage": cpuPercent,
            "usage_percentage_detail": cpuPercentTargetting
        }
        
        return Resource(memory=memory, cpu=cpu, disk=disk, unit=unit)