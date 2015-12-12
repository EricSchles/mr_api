from flask_restful import Resource, reqparse

def install(app):
    app.add_resource(MRApi, '/')

def foo(text):
    return True

class MRApi(Resource):
    def get(self):
        parser = reqparse.RequestParser()
        parser.add_argument('text',
                            type=str,
                            help='Text from message')
        args = parser.parse_args()
        text = args['text']
        response = foo(text)
        return {'response': response}

