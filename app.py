from flask import Flask
from flask_restful import Api, Resource
from firebase import sprint_message

app = Flask(__name__)
api = Api(app)

class DeadlineListRes(Resource):
    def post(self):
        return {
            'response_type': 'in_channel',
            'text': sprint_message(),
        }

api.add_resource(DeadlineListRes, '/slack/deadlines')

if __name__ == '__main__':
    app.run(debug=True)