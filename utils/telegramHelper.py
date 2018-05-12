# This file is for accessing telegram related apis

import requests
import json

TELEGRAM_SECRET_TOKEN = "554116144:AAE50o8iZwybG-xCRpYRNplqMvIX9AF3OQs"

def getBaseURL():
	return "https://api.telegram.org/bot" + TELEGRAM_SECRET_TOKEN + "/"

def getHeaders():
	headers = {}
	headers['Content-Type'] = 'application/json'
	return headers

def setWebhooks():
	requestURL = getBaseURL() + "setWebhook"
	headers = getHeaders()

	data = {}
	data['url'] = "https://dry-dusk-42163.herokuapp.com/receiveMessage"
	data['max_connections'] = 30
	jsonData = json.dumps(data)

	#req = urllib.request.Request(requestURL)
	#req.add_header('Content-Type', 'application/json')
	response = requests.post(requestURL, data = data, headers = headers)
	return response.status_code