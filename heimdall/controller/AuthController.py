from flask_restful import Api, Resource


class AuthController(Resource):

    def get(self):
        """ Minimal endpoint for check if server is up """
        resp = {}
        resp['message'] = "Nobody"
        return resp
