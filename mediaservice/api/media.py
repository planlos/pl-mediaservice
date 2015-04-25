from flask.ext.restful import Resource
from flask import make_response, jsonify


class Media_Api(Resource):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

    def get(self, cmd = None):
        if cmd == "_status":
            response = dict(
                msg = "mediaservice status",
                documents = 1
            )
        else:
            response = dict(
                msg = "Hello, this is mediaservice"
            )
        return make_response(jsonify(response))

    def post(self):
        pass


class Media_Object_Api(Resource):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

    def get(self, cmd = None):
        if cmd == "_status":
            response = dict(
                msg = "mediaservice status",
                documents = 1
            )
        else:
            response = dict(
                msg = "Hello, this is mediaservice"
            )
        return make_response(jsonify(response))

    def post(self):
        pass
