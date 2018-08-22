from flask import Flask
from flask_restful import Api, Resource
from google.cloud import firestore

app = Flask(__name__)
api = Api(app)

class DeadlineListRes(Resource):
    def get(self):
        return {
            'response_type': 'in_channel',
            'text': 'Deadline is comming',
        }
    
    def post(self):
        return {
            'response_type': 'in_channel',
            'text': 'Deadline is comming (POST)',
        }

api.add_resource(DeadlineListRes, '/slack/deadlines')

if __name__ == '__main__':
    app.run(debug=True)