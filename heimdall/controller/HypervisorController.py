from heimdall.framework.model.Endpoint import *

from heimdall.decorator.Auhentication import hasRole
from heimdall.model.Role import Role
from heimdall.service.HypervisorService import HypervisorService

class HypervisorController(Endpoint):

    def __init__(self) -> None:
        self.hypervisorService = HypervisorService()

    @hasRole(Role.ADMIN)
    def get(self):
        resp = {
            "informations": self.hypervisorService.hyperviseurInfo(),
        }
        return SuccessResponse(HttpStatus.OK,resp)
