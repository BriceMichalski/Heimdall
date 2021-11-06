from flask import Flask,g
from flask_restful import Api

from heimdall.framework.resources.Configuraton import Configuration

import yaml

class HeimdallServer():

    def __init__(self) -> None:
        """ heimdall server constructor"""
        self.config = Configuration()
        self.app = Flask(__name__)

        self.api = Api(self.app)

    def run(self):
        """ Start server """
        with self.app.app_context():
            # Load router
            self.loadRouter()
            self.app.run(
                host=self.config.server.host,
                port=self.config.server.port, 
                debug=self.config.server.debug
            ) 


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
