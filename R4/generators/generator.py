from fhir.resources.meta import Meta
from randomizer.randomizer import *




class Generator:

	def set_meta(self, url, resource):
		meta = Meta()
		meta.profile = [url]
		resource.meta = meta

	def set_status(self, resource):
		resource.status = RandomStatus.next(RandomStatus)


