from heimdall.framework.model.meta.Singleton import Singleton
from heimdall.model.DomainRepresentation import DomainRespresentation
from heimdall.exception.ObjectNotFound import DomainNotFound


import libvirt

class DomainService(metaclass=Singleton):
    
    def __init__(self) -> None:
        self.conn = libvirt.open("qemu:///system")

    def getDomainList(self):
        domains = self.conn.listAllDomains()

        domainList = [
            DomainRespresentation(domain) for domain in domains
        ]
        
        return domainList

    
    def findById(self,domainUUID):
        try:
            domain = self.conn.lookupByUUIDString(domainUUID)
            return domain
        except libvirt.libvirtError as e:
            if "Domain not found" in str(e):
                raise DomainNotFound(str(e))


    def deleteDomainById(self,domainUUID):
        domain = self.findById(domainUUID)