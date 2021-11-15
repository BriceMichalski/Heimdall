from heimdall.framework.resources.Configuraton import Configuration
from heimdall.framework.model.meta.Singleton import Singleton

from heimdall.model.User import User
from heimdall.model.Role import Role
from heimdall.model.Authentication import Authentication

from flask_jwt_extended import create_access_token, create_refresh_token
from flask_jwt_extended import JWTManager

from flask import current_app 

class AuthService(metaclass=Singleton):

    def __init__(self) -> None:
        self.config = Configuration()
        self.jwt = JWTManager(current_app)

    def getTokenIfValidCredential(self, username, password) -> Authentication:

        if username == self.config.security.admin.username and password == self.config.security.admin.password:
            client = User(username,roles=[Role.ADMIN])
            accessToken = create_access_token(
                identity=client.username,
                additional_claims={
                    "roles" : client.roles
                }
            )
            refreshToken = create_refresh_token(
                identity=client.username,
                additional_claims={
                    "roles" : client.roles
                }
            )

            return Authentication(accessToken,refreshToken)
        else:
            return None