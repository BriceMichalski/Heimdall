from heimdall.exception.DefinitionConflictException import DefinitionConflictException
from heimdall.exception.ObjectNotFound import BaseImageNotFound
from heimdall.exception.ChecksumException import ChecksumException
from heimdall.exception.AlreadyExistException import AlreadyExistException
from heimdall.framework.model.Endpoint import *
from heimdall.service.BaseImageService import BaseImageService

from heimdall.decorator.Auhentication import hasRole
from heimdall.model.Role import Role

class BaseImageController(Endpoint):

    def __init__(self) -> None:
        self.biService = BaseImageService()
        
    @hasRole(Role.ADMIN)
    @RequestArgs([
        Argument("url", required=True, help="Base image url cannot be null"),
        Argument("name",required=True, help="Base image name cannot be null"),
        Argument("family", required=True, help="Base image family cannot be null"),
        Argument("variant",required=True, help="Base image variant cannot be null"),
        Argument("md5sum", required=True, help="Base image checksum cannot be null"),
    ])
    def post(self,args):
        try:
            image = self.biService.newBaseImage(args)
            return SuccessResponse(HttpStatus.CREATED,image)
        except AlreadyExistException as e:
            return ErrorResponse(HttpStatus.CONFLICT,str(e))
        except ChecksumException as e:
            return ErrorResponse(HttpStatus.BAD_REQUEST,str(e))

    @hasRole(Role.ADMIN)
    def get(self):
        images = self.biService.getImageList()

        return SuccessResponse(HttpStatus.OK,images)

    @hasRole(Role.ADMIN)
    @RequestArgs([
        Argument("uuid", required=True, help="base image uuid cannot be null"),
        Argument("name",required=True, help="Base image name cannot be null"),
    ])
    def delete(self,args):
        try:
            uuid = args.get('uuid')
            name = args.get('name')
            self.biService.delete(uuid,name)
            return SuccessResponse(HttpStatus.NO_CONTENT)
        except BaseImageNotFound as e:
            return ErrorResponse(HttpStatus.NOT_FOUND,str(e))
        except DefinitionConflictException as e:
            return ErrorResponse(HttpStatus.BAD_REQUEST,str(e))