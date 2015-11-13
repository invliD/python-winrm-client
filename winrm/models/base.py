from winrm import uris

class BaseModel(object):

	NAMESPACE_URI = uris.WINRM_URI

	@classmethod
	def resource_uri(cls):
		return '{}/{}'.format(cls.NAMESPACE_URI, cls.CLASS_NAME)
