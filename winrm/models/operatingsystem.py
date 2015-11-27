from winrm.models.base import BaseModel


class OperatingSystem(BaseModel):

	CLASS_NAME = 'Win32_OperatingSystem'

	def __init__(self, number_of_processes=None, free_physical_memory=None, free_virtual_memory=None, total_physical_memory=None, total_virtual_memory=None):
		self.number_of_processes = number_of_processes
		self.free_physical_memory = free_physical_memory
		self.free_virtual_memory = free_virtual_memory
		self.total_physical_memory = total_physical_memory
		self.total_virtual_memory = total_virtual_memory

	def __str__(self):
		return 'OperatingSystem'

	@classmethod
	def from_dict(cls, d):
		return cls(
			number_of_processes=int(d['NumberOfProcesses']),
			free_physical_memory=int(d['FreePhysicalMemory']) * 1024,
			free_virtual_memory=int(d['FreeVirtualMemory']) * 1024,
			total_physical_memory=int(d['TotalVisibleMemorySize']) * 1024,
			total_virtual_memory=int(d['TotalVirtualMemorySize']) * 1024,
		)
