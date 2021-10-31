from os import path
from flask_restful import Api
from heimdall.controller.HealthController import HealthController

import yaml

ROUTE_FILE = 'heimdall/config/routes.yml' 

class Router:

    def __init__(self, api: Api) -> None:
        self.api = api

    def routeRegistration(self): 
        self.staticRouteRegistration()
        self.dynamicRouteRegistration()
       
    def staticRouteRegistration(self): 
        self.registerRoute(HealthController, "/health")

    def dynamicRouteRegistration(self):
        routes = self.getDynamicRouteConfig()
        for route in routes:
            try:
                controllersModule = __import__('heimdall.controller', fromlist=[route.get("controller")])
                specificControllerModule = getattr(controllersModule, route.get("controller"))
                controller = getattr(specificControllerModule,route.get("controller"))

                self.registerRoute(controller, route.get("path"))
            except Exception as exc:
                error = "Error during {name} import in router : ".format(name=route.get("controller"))
                print(error) # TODO : use logger
                print(exc)
    
    def registerRoute(self, klass ,path :str) -> None:
        self.api.add_resource(klass, path)
        print("Route succesfully register for path " + path)

    def getDynamicRouteConfig(self) -> list:
        routes = []

        with open(ROUTE_FILE, "r") as stream:
            try:
                config = yaml.safe_load(stream)
                try: 
                    routesConfig = config.get("routes")

                    for route in routesConfig:
                        routes.append({
                            "path": route.get("path"),
                            "controller": route.get("controller")
                        })
                except Exception as exc:
                    print(exc) # TODO : use logger

            except yaml.YAMLError as exc:
                print(exc) # TODO : use logger
        
        return routes