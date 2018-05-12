from flask.views import MethodView
from flask import request
import json

class ReceiveMessageHander(MethodView):
	def post(self):
		return "Complete Request :: " + request.get_data(as_text=True)