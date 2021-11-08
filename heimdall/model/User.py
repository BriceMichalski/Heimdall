from heimdall.framework.model.ApiResource import ApiResource

class User(ApiResource):
    
    _DTO_BLACKLIST= ["password"]

    def __init__(self, username :str, password :str =None, email :str =None , roles :list =[]) -> None:
        self.username = username
        self.password = password
        self.email = email
        self.roles = roles 

        
