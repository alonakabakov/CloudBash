import flask
import flask_restful


def request_validation(data, *keys):
    pass

class Example(flask_restful.Resource):
    def get(self):
        return 'hello'

    def post(self):
        return ''

    def put(self):
        return ''

    def delete(self):
        return ''
