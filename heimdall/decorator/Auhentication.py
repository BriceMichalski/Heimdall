from functools import wraps

from flask import current_app 
from flask_jwt_extended import JWTManager
from flask_jwt_extended import verify_jwt_in_request
from flask_jwt_extended import get_jwt
from flask_jwt_extended.exceptions import NoAuthorizationError
from jwt.exceptions import ExpiredSignatureError, InvalidSignatureError

from heimdall.framework.model.Endpoint import ErrorResponse
from heimdall.framework.model.HttpStatus import HttpStatus
from heimdall.model.Role import Role

def hasRole(target):

    JWTManager(current_app)
    roleRef = Role()

    def decorator(function):
        @wraps(function)
        def wrapper(*args, **kwargs):
            authorized = False

            try :
                verify_jwt_in_request()
            except NoAuthorizationError:
                return ErrorResponse(HttpStatus.UNAUTHORIZE,"Missing Authorization header")
            except ExpiredSignatureError:
                return ErrorResponse(HttpStatus.UNAUTHORIZE,"Token signature has expired")
            except InvalidSignatureError:
                return ErrorResponse(HttpStatus.UNAUTHORIZE,"Signature verification failed")

            claims = get_jwt()
            roles = claims.get('roles')
            
            if roles == None:
                return ErrorResponse(HttpStatus.UNAUTHORIZE,"Unable to find roles claims")

            for role in roles :
                targetIsPresent = roleRef.hasRole(role,target)
                if targetIsPresent:        
                    authorized = True
                    break

            if authorized:  
                return function(*args, **kwargs)

            return ErrorResponse(HttpStatus.UNAUTHORIZE,"You haven't sufficient privilege")

        return wrapper
    return decorator