from flask_restful import Api

from heimdall.controller.HealthController import HealthController

class Router:

    def __init__(self, api: Api) -> None:
        self.api = api

    def routeRegistration(self): 
        self.api.add_resource(HealthController, "/health")
