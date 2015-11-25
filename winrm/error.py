class WinRMError(Exception):

	def __init__(self, code, msg):
		super(Exception, self).__init__(msg)
		self.code = code
