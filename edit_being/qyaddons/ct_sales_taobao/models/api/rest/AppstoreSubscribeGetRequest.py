'''
Created by auto_sdk on 2016.04.13
'''
from base import RestApi
class AppstoreSubscribeGetRequest(RestApi):
	def __init__(self,domain='gw.api.taobao.com',port=80):
		RestApi.__init__(self,domain, port)
		self.lease_id = None
		self.nick = None

	def getapiname(self):
		return 'taobao.appstore.subscribe.get'
