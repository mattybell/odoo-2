'''
Created by auto_sdk on 2014.02.08
'''
from base import RestApi
class PictureReplaceRequest(RestApi):
	def __init__(self,domain='gw.api.taobao.com',port=80):
		RestApi.__init__(self,domain, port)
		self.image_data = None
		self.picture_id = None

	def getapiname(self):
		return 'taobao.picture.replace'

	def getMultipartParas(self):
		return ['image_data']
