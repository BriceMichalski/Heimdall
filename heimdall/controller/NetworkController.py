from heimdall.framework.model.Endpoint import *

from heimdall.decorator.Auhentication import hasRole
from heimdall.exception.DefinitionConflictException import DefinitionConflictException
from heimdall.exception.ObjectNotFound import NetworkNotFound
from heimdall.model.Role import Role
from heimdall.service.NetworkService import NetworkService


class NetworkController(Endpoint):

    def __init__(self) -> None:
        self.networkService = NetworkService()

    @hasRole(Role.ADMIN)
    def get(self):
        networkList = self.networkService.getNetworkList()
        return SuccessResponse(HttpStatus.OK,networkList)

    @hasRole(Role.ADMIN)
    @RequestArgs([
        Argument("name", required=True, help="Netwok name cannot be null"),
        Argument("bridge",required=True, help="Netwok bridge cannot be null"),
        Argument("forwardMode", required=True,  help="forwardMode cannot be null"),
        Argument("ipAdress", required=True,  help="ipAdress cannot be null"),
        Argument("netmask", required=True,  help="netmask cannot be null"),
        Argument("dhcpStart", required=True,  help="dhcpStart cannot be null"),
        Argument("dhcpEnd", required=True,  help="dhcpEnd cannot be null")
    ])
    def post(self,args):
        try: 
            networkRep = self.networkService.createNetwork(args)
                
            resp = {}
            resp["message"] = "Network Created"
            resp["network"] = networkRep

            return SuccessResponse(HttpStatus.CREATED,resp)
        except Exception as e:
            return ErrorResponse(HttpStatus.INTERNAL_ERROR,str(e))

    @hasRole(Role.ADMIN)
    @RequestArgs([
        Argument("name", required=True, help="Netwok name cannot be null"),
        Argument("uuid",required=True, help="Netwok uuid cannot be null"),
    ])
    def delete(self,args):
        try: 
            self.networkService.deleteNetwork(args)
            return SuccessResponse(HttpStatus.NO_CONTENT)
        except DefinitionConflictException as e:
            return ErrorResponse(HttpStatus.BAD_REQUEST,str(e))
        except NetworkNotFound as e:
            return ErrorResponse(HttpStatus.NOT_FOUND,str(e))
        except Exception as e:
            return ErrorResponse(HttpStatus.INTERNAL_ERROR,str(e))