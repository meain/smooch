from flask import Flask, request, jsonify
from flask_cors import CORS
from functools import wraps
import inspect


class Synapse(object):
    def __init__(self, cors=False):
        self.__name__ = 'synapse'
        self.app = Flask(__name__)
        if cors:
            CORS(self.app)

    def _validate_user(self, headers, data):
        pass

    def _validate_input(self, data, args, defaults):
        non_keys = []
        length = len(args)
        if defaults is not None:
            length = len(args) - len(defaults)
        args = args[:length]  # remove kwargs
        for key in list(args):
            if key not in data:
                non_keys.append(key)
        if len(non_keys) == 0:
            return True, []
        else:
            return False, non_keys

    def connect(self, endpoint, methods=['GET', 'POST']):
        def flask_wrapper_outer(fn, *args):
            @wraps(fn)
            def flask_wrapper_inner(*args, **kwargs):
                valid, non_keys = self._validate_input(
                    request.json,
                    inspect.getargspec(fn).args,
                    inspect.getargspec(fn).defaults)
                if not valid:
                    return jsonify({
                        "success": False,
                        "error": f"Keys {str(non_keys)} not found"
                    })
                response = fn(**request.json)
                return jsonify({
                    "success": True,
                    "data": response,
                })

            return self.app.add_url_rule(
                endpoint, view_func=flask_wrapper_inner, methods=methods)

        return flask_wrapper_outer

    def start(self, **kwargs):
        self.app.run( **kwargs)
