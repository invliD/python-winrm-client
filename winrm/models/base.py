from winrm import uris

class BaseModel(object):

	NAMESPACE_URI = uris.WINRM_URI

	@classmethod
	def resource_uri(cls):
		return '{}/{}'.format(cls.NAMESPACE_URI, cls.CLASS_NAME)

	def __repr__(self):
		return '{}({})'.format(
			self.__class__.__name__,
			', '.join('{}={}'.format(
				k, repr(v))
				for (k,v) in self.__dict__.iteritems()
				if v is not None
			)
		)
