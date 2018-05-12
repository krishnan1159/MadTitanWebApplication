from flask.views import MethodView
from flask import request
import json
import logging

class ReceiveMessageHander(MethodView):
	def post(self):
		logging.error('++++ I told you so' + request.get_data(as_text=True))
		return "Complete Request :: " + request.get_data(as_text=True)