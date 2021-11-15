from libvirt import virDomain
from heimdall.framework.model.ApiResource import ApiResource

from heimdall.helper.SizeUnit import SizeUnit
from heimdall.helper.DomainStateMapper import DomaineStateMapper


class DomainRespresentation(ApiResource):

    def __init__(self,domain :virDomain) -> None:
        state, maxmem, mem, cpus, cput = domain.info()
        unitHelper = SizeUnit()
        domainState = DomaineStateMapper()

        self.name= domain.name()
        self.uuid= domain.UUIDString()
        self.info = {
            "state": domainState.toString(state),
            "memory_size": unitHelper.convertUnit(maxmem,SizeUnit.KB,SizeUnit.MB),
            "memory_unit": SizeUnit.MB.get("symbol"),
            "cpu_count": cpus
        }
