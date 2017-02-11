import requests
import json

F2F_KEY = "key"
F2F_SEARCH = "q"
F2F_GET = "rId"
F2F_AUTH_KEY = "6559a12bd8da9944c039581db866d54d"
F2F_URL_SEARCH = "http://food2fork.com/api/search"
F2F_URL_GET = "http://food2fork.com/api/get"

class F2F_poller(object):
	
	def __init__(self, id):
		self.id = id
		return

	def get(self):
		param = {F2F_KEY: F2F_AUTH_KEY, F2F_GET, self.id}
		return requests.get(F2F_URL_GET, param).json()
