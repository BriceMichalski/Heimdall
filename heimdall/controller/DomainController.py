from heimdall.exception.ObjectNotFound import DomainNotFound
from heimdall.framework.model.Endpoint import *

from heimdall.decorator.Auhentication import hasRole
from heimdall.model.Role import Role
from heimdall.service.DomainService import DomainService,DomainRespresentation

class DomainController(Endpoint):

    def __init__(self) -> None:
        self.domainService = DomainService()

    @hasRole(Role.ADMIN)
    def get(self,domainUUID):
        try:
            domain = DomainRespresentation(self.domainService.findById(domainUUID))
            return SuccessResponse(HttpStatus.OK,domain)
        except DomainNotFound as e:
            return ErrorResponse(HttpStatus.NOT_FOUND,str(e))

    def delete(self,domainUUID):
        domain = self.domainService.deleteDomainById(domainUUID)
        
        