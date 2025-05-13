from . import app
import sqlite3
from flask import request

class InterceptRequestMiddleware:
    def __init__(self, wsgi_app):
        self.wsgi_app = wsgi_app

    def __call__(self, environ, start_response):
        environ['Access-Control-Allow-Origin'] = '*'
        return self.wsgi_app(environ, start_response)





@app.route("/", methods=["GET"])
def ind():
    return "hello"

@app.route("/start", methods=["GET"])
def start():
    pass



def convertToKML():
    
    pass