from heimdall.framework.model.ApiRessource import ApiRessource

class Authentication(ApiRessource):

    def __init__(self,token,refreshToken) -> None:
        self.access_token = token
        self.refresh_token = refreshToken




