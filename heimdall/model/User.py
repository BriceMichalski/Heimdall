from heimdall.framework.model.ApiRessource import ApiRessource
from heimdall.model.Role import Role

class User(ApiRessource):
    
    _DTO_BLACKLIST= ["password"]

    def __init__(self, username :str, password :str =None, email :str =None , roles :list =[]) -> None:
        self.username = username
        self.password = password
        self.email = email
        self.roles = roles 

        
