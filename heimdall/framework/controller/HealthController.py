from flask_restful import Resource

class HealthController(Resource):

    def get(self):
        """ Minimal endpoint for check if server is up """
        resp = {}
        resp['message'] = "Heimdall alive"
        resp['status'] = "UP"
        return resp
