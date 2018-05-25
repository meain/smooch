from flask import Flask
from functools import wraps
# CORS is optional?

class Synapse(object):
    def __init__(self):
        self.__name__ = 'synapse'
        self.app = Flask(__name__)

    def connect(self, endpoint):
        def flask_wrapper_outer(fn):
            @wraps(fn)
            @self.app.route(endpoint)
            def flask_wrapper_inner(*args, **kwargs):
                print (endpoint, fn.__name__, args, kwargs)
                response = fn('hai')  # send verified resp
                # print ( response )
                return response
            return flask_wrapper_inner
        return flask_wrapper_outer

    def start(self, url='0.0.0.0', port=8080, **kwargs):
        self.app.run(host=url, port=port, **kwargs)

