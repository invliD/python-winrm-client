from winrm import uris
from winrm.models.base import BaseModel


class SmartData(BaseModel):

	NAMESPACE_URI = uris.WMI_URI
	CLASS_NAME = 'MSStorageDriver_ATAPISmartData'

	def __init__(self, vendor_data=None):
		self.vendor_data = vendor_data

	def __str__(self):
		return "SmartData"

	@classmethod
	def from_dict(cls, d):
		print(repr(d))
		return cls(
			vendor_data=tuple(int(d) for d in d['VendorSpecific']),
		)
