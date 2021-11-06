from flask_restful import Resource as Endpoint
from flask_restful import abort
from flask_restful.reqparse import Argument
from flask import g

from heimdall.framework.decorator.Endpoint import RequestArgs
from heimdall.framework.model.HttpStatus import HttpStatus
from heimdall.framework.model.ApiRessource import ApiRessource

__all__ = [
    "Endpoint",
    "abort",
    "Argument",
    "g",
    "RequestArgs",
    "HttpStatus",
    "ErrorResponse",
    "SuccessResponse"
]

def ErrorResponse(code :HttpStatus =HttpStatus.INTERNAL_ERROR,msg :str = "Something went wrong. (INTERNAL_SERVER_ERROR)"):
    resp = {
        "message": msg,
        "status": code
    }

    return resp,code


def SuccessResponse(code :HttpStatus =HttpStatus.OK, body ="OK"):

    if type(body) is str:
        resp = {
            "message": body
        }

    elif issubclass(type(body),ApiRessource):
        resp = body.asDict()

    else:
        resp = body


    return resp,code