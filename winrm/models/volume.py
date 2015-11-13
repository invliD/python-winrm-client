from winrm.models.base import BaseModel


class DriveType(object):

	"""Drive type of a Volume.

	See https://msdn.microsoft.com/en-us/library/aa394515(v=vs.85).aspx
	"""

	UNKNOWN = 0
	NO_ROOT_DIRECTORY = 1
	REMOVABLE_DISK = 2
	LOCAL_DISK = 3
	NETWORK_DRIVE = 4
	COMPACT_DISC = 5
	RAM_DISC = 6


class Volume(BaseModel):

	CLASS_NAME = 'Win32_Volume'

	def __init__(self, label=None, caption=None, drive_letter=None, description=None, capacity=None, free_space=None, type=None, file_system=None):
		self.label = label
		self.caption = caption
		self.drive_letter = drive_letter
		self.description = description
		self.capacity = capacity
		self.free_space = free_space
		self.type = type
		self.file_system = file_system

	def __str__(self):
		return self.label

	def __repr__(self):
		return 'Volume({})'.format(', '.join('{}={}'.format(k, repr(v)) for (k,v) in self.__dict__.iteritems() if v is not None))

	@classmethod
	def from_dict(cls, d):
		return cls(
			label=d['Label'],
			caption=d['Caption'],
			drive_letter = d['DriveLetter'],
			description = d['Description'],
			capacity = int(d['Capacity']),
			free_space = int(d['FreeSpace']),
			type = int(d['DriveType']),
			file_system = d['FileSystem'],
		)
