from heimdall.framework.model.Endpoint import *

from heimdall.decorator.Auhentication import hasRole
from heimdall.model.Role import Role
from heimdall.service.ResourceService import ResourceService

class ResourceController(Endpoint):

    def __init__(self) -> None:
        self.resourceService = ResourceService()

    @hasRole(Role.ADMIN)
    @RequestArgs([
        Argument("unit",required=False,default="B")
    ])
    def post(self,args):
        symbol = args.get('unit')
        resource = self.resourceService.getResources(symbol)
        return SuccessResponse(HttpStatus.OK,resource)
