from heimdall.framework.model.Endpoint import *

from heimdall.service.ResourceService import ResourceService

class ResourceController(Endpoint):

    def __init__(self) -> None:
        self.resourceService = ResourceService()

    @RequestArgs([
        Argument("unit",required=False,default="B")
    ])
    def post(self,args):
        symbol = args.get('unit')
        resource = self.resourceService.getResources(symbol)
        return SuccessResponse(HttpStatus.OK,resource)
