from fhir.resources.diagnosticreport import DiagnosticReport
from fhir.resources.meta import Meta
from R4.randomizer.randomizer import *




class Generator:

	def set_meta(self, url, resource):
		meta = Meta.construct()
		meta.profile = [url]
		resource.meta = meta

	def set_status(self, resource):
		resource.status = RandomStatus.next(RandomStatus)


