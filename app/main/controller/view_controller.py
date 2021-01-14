from flask.helpers import make_response
from flask_restx import Namespace, Resource
from flask import render_template

api = Namespace("view", description="view related operations")

@api.route("/index")
class index(Resource):
    @api.doc("index")
    def get(self):
        headers = {'Content-Type': 'text/html'}
        return make_response(render_template('index.html'), 200, headers)

    def post(self):
        return render_template('index.html')
