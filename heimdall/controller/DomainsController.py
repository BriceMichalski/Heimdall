from heimdall.framework.model.Endpoint import *

from heimdall.decorator.Auhentication import hasRole
from heimdall.model.Role import Role
from heimdall.service.DomainService import DomainService

class DomainsController(Endpoint):

    def __init__(self) -> None:
        self.domainService = DomainService()

    @hasRole(Role.ADMIN)
    def get(self):
        domainList = self.domainService.getDomainList()

        return SuccessResponse(HttpStatus.OK,domainList)