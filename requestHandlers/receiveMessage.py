from flask.views import MethodView
from flask import request
import json
import logging
import threading
from utils.telegramHelper import sendMessage

class ReceiveMessageHander(MethodView):
	def post(self):
		logging.error('++++ I told you so' + request.get_data(as_text=True))
		requestJSON = request.get_json()
		#logging.error("RequestJSON = " + requestJSON)
		self.handleMessage(requestJSON)
		return ''

	def handleMessage(self, requestJSON):
		if (requestJSON == None):
			logging.error("ERROR: Invalid JSON Request data from telegram")
			return ''

		# Find the message type text, command etc.
		telegramMessage = requestJSON['message']
		chatID = telegramMessage['chat']['id']
		chatText = telegramMessage['text']

		logging.error(" ChatInfo : chatID = " + str(chatID) + ", chatText = " + chatText)

		responseMessage = "We will get back shortly!!!"
		response = sendMessage(chatID, responseMessage)
		if response.status_code != 200:
			logging.error("++++ Something went wrong when sending message")
		return 'OK'
