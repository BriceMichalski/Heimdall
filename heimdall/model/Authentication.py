from heimdall.framework.model.ApiResource import ApiResource

class Authentication(ApiResource):

    def __init__(self,token,refreshToken) -> None:
        self.access_token = token
        self.refresh_token = refreshToken




