'''
Created by auto_sdk on 2015.09.17
'''
from base import RestApi
class ItemQuantityUpdateRequest(RestApi):
	def __init__(self,domain='gw.api.taobao.com',port=80):
		RestApi.__init__(self,domain, port)
		self.fields = None

	def getapiname(self):
		return 'taobao.item.quantity.update'
