from winrm.models.base import BaseModel


class PerfDataProcessor(BaseModel):

	CLASS_NAME = 'Win32_PerfFormattedData_PerfOS_Processor'

	def __init__(self, name=None, percent_processor_time=None, percent_idle_time=None):
		self.name = name
		self.percent_processor_time = percent_processor_time
		self.percent_idle_time = percent_idle_time

	def __str__(self):
		return self.name

	@classmethod
	def from_dict(cls, d):
		return cls(
			name=d['Name'],
			percent_processor_time=int(d['PercentProcessorTime']),
			percent_idle_time=int(d['PercentIdleTime']),
		)
