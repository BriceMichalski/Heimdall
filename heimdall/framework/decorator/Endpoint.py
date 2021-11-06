from flask_restful import reqparse
from functools import wraps

def RequestArgs(argumentsToParse):
    """ 
        Décorator for flask_restful.Resource class method that allow request argument parsing and inject it in the fonction
        :param argumentsToParse: Array of flask_restful.reqparse.Argument
    
        usage exemple: 

            @RequestArgs([
                    Argument("username",required=True,help="Username cannot be null"),
                    Argument("password",required=True,help="Password cannot be null")
            ])
            def post(self,args):

                username = args.get("username",None)
                password = args.get("password",None)
    
    """
    def decorator(function):
        @wraps(function)
        def wrapper(inst):
            parser = reqparse.RequestParser()
            parser.args = argumentsToParse
            arguments = parser.parse_args()
            
            return function(inst,arguments)            
        return wrapper
    return decorator

        
    