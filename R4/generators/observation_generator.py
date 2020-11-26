from fhir.resources.diagnosticreport import *
from fhir.resources.codeableconcept import CodeableConcept
from fhir.resources.coding import Coding
from fhir.resources.fhirdate import FHIRDate
from fhir.resources.fhirreference import FHIRReference
from fhir.resources.identifier import Identifier
from fhir.resources.observation import Observation

from randomizer.randomizer import *
from generators.generator import Generator


class ObservationGenerator():
  def __init__(self):
    pass

  def next(self):
    pass


class ObservationLabGenerator(Generator):

	def __init__(self):
		self.observation = Observation()
		self.url = "https://www.medizininformatik-initiative.de/fhir/core/modul-labor/StructureDefinition/ObservationLab"

	def next(self):
		print(self.url)
		Generator.set_meta(self, self.url, self.observation)
		Generator.set_status(self, self.observation)
		self.__set_identifier()
		print(self.observation.as_json())
		return self.observation

	def __set_identifier(self):
		identifier = Identifier()
		assigner_identifier = Identifier()
		coding = Coding()
		coding.system = "http://terminology.hl7.org/CodeSystem/v2-0203" #fixed
		coding.code = "OBI" #fixed
		generate_codeable_concept = CodeableConcept()
		generate_codeable_concept.coding = [coding]
		identifier.type = generate_codeable_concept
		reference = FHIRReference({"identifier":{ "system": "https://www.medizininformatik-initiative.de/fhir/core/NamingSystem/org-identifier", "value": "DIZ-ID"}})
		identifier.assigner = reference
		identifier.system = "https://diz.mii.de/fhir/core/NamingSystem/test-lab-results"
		identifier.value = "59826-8_1234567890" # TODO randomize
		self.observation.identifier = [identifier]

