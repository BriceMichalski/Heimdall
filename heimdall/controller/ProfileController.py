from heimdall.framework.model.Endpoint import *

from heimdall.model.User import User


class ProfileController(Endpoint):

    def __init__(self) -> None:
        super().__init__()

    @RequestArgs([
        Argument("username", required=True,  help="Username cannot be null"),
        Argument("password", required=True,  help="Password cannot be null"),
        Argument("email",    required=False, help="Email cannot be null")
    ])
    def post(self,args):
        username = args.get("username",None)
        password = args.get("password",None)
        email= args.get("email",None)

        user = User(username,password,email)

        return user.asDict,HttpStatus.OK
