'''
Created by auto_sdk on 2016.03.04
'''
from base import RestApi
class WlbWmsConsignOrderConfirmRequest(RestApi):
	def __init__(self,domain='gw.api.taobao.com',port=80):
		RestApi.__init__(self,domain, port)
		self.content = None

	def getapiname(self):
		return 'taobao.wlb.wms.consign.order.confirm'
