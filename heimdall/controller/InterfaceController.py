from heimdall.framework.model.Endpoint import *

from heimdall.decorator.Auhentication import hasRole
from heimdall.model.Role import Role
from heimdall.service.NetworkService import NetworkService


class InterfaceController(Endpoint):

    def __init__(self) -> None:
        self.networkService = NetworkService()

    @hasRole(Role.ADMIN)
    def get(self):
        interfaceList = self.networkService.getInterfaceList()

        return SuccessResponse(HttpStatus.OK,interfaceList)
