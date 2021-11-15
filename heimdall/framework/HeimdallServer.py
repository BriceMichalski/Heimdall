from heimdall.framework.resources.Database import DatabaseConnection
from flask import Flask,g
from flask_restful import Api

from heimdall.framework.resources.Configuraton import Configuration
from heimdall.framework.resources.JsonEncoder import JsonEncoder

import os

class HeimdallServer():

    def __init__(self) -> None:
        """ heimdall server constructor"""
        self.config = Configuration()
        self.app = Flask(__name__)
        self.api = Api(self.app)
        self.database = DatabaseConnection()
        
    def run(self):
        """ Start server """
        with self.app.app_context():
            self.requirement()
            self.configFlask()
            self.loadRouter()
            self.app.run(
                host=self.config.server.host,
                port=self.config.server.port, 
                debug=self.config.server.debug
            ) 

    def requirement(self):
        if not os.path.isdir(self.config.workingDir):
            os.mkdir(self.config.workingDir)

    def configFlask(self):
        self.app.json_encoder = JsonEncoder
        self.app.config["RESTFUL_JSON"] = {'cls': JsonEncoder}
        self.app.config["SECRET_KEY"] = self.config.server.secret
        self.app.config["JWT_ACCESS_TOKEN_EXPIRES"] = self.config.security.jwt_ttl_minutes * 60


    def loadRouter(self):
        """ Router loading
            
            In order this fonction will :

            1 - Load default configuration file located at ./resources/application.yml
            2 - Override flask config with this application.yml section if exist
            3 - Load router

        """
        from heimdall.framework.resources.Router import Router
        self.router = Router(self.api)
        self.router.routeRegistration()
