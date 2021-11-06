from heimdall.model.Authentication import Authentication
from heimdall.framework.model.Endpoint import *
from heimdall.service.AuthService import AuthService

class AuthController(Endpoint):

    def __init__(self) -> None:
        super().__init__()
        self.authService = AuthService()
        

    @RequestArgs([
        Argument("username", required=True,  help="Username cannot be null"),
        Argument("password", required=True,  help="Password cannot be null"),
    ])
    def post(self,args):
       
        username = args.get("username",None)
        password = args.get("password",None)

        authentication :Authentication = self.authService.getTokenIfValidCredential(username,password)

        if authentication != None:
            return SuccessResponse(HttpStatus.CREATED,authentication)
        else:
            return ErrorResponse(HttpStatus.UNAUTHORIZE,"Bad username or password")

