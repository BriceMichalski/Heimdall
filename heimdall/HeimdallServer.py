from flask import Flask
from flask_restful import Api
from flask_jwt_extended import JWTManager
from flask_bcrypt import Bcrypt

import yaml

class HeimdallServer():

    def __init__(self) -> None:
        """ heimdall server constructor"""
        self.app = Flask(__name__)
        self.api = Api(self.app)
        self.bcrypt = Bcrypt(self.app)
        self.jwt = JWTManager(self.app)
        self.config = {}

    def configuration(self):
        """ heimdall server configuration
            
            In order this fonction will :

            1 - Load default configuration file located at ./resources/application.yml
            2 - Override flask config with this application.yml section if exist
            3 - Load router
        
        """
        # Load config file
        logFilePath = 'heimdall/resources/application.yml'
        self.config = self.loadConfigFile(logFilePath)

        # Override Flask default configuraton
        if self.config.get('app') != None:
            self.app.config = self.config.get('app')

        # Load router
        self.loadRouter()

    def run(self):
        """ Start server with configuration found in application.yml """
        self.app.run(
            host=self.config.get('server').get('host'),
            port=self.config.get('server').get('port'), 
            debug=self.config.get('server').get('debug')
        )

    def loadRouter(self):
        """ Router loading
            
            In order this fonction will :

            1 - Load default configuration file located at ./resources/application.yml
            2 - Override flask config with this application.yml section if exist
            3 - Load router

        """
        from heimdall.resources.Router import Router
        self.router = Router(self.api)
        self.router.routeRegistration()


    def loadConfigFile(self,path: str) -> dict:
        with open(path, "r") as stream:
            try:
                return yaml.safe_load(stream)
            except yaml.YAMLError as exc:
                print(exc)
        
