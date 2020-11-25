from fhir.resources.diagnosticreport import *
from fhir.resources.codeableconcept import CodeableConcept
from fhir.resources.coding import Coding
from fhir.resources.meta import Meta
from fhir.resources.fhirdate import FHIRDate
from fhir.resources.fhirreference import FHIRReference
from fhir.resources.identifier import Identifier

from randomizer.randomizer import *
from random import *



class DiagnosticReportGenerator():

	def __init__(self, status = RandomStatus(), loinc = RandomLoinc()):
		self.random_status = status		
		self.random_loinc = loinc		

	def next(self, id):
		diagnostic_report = DiagnosticReport()
		diagnostic_report.id = str(id)
		diagnostic_report.status = self.random_status.next()
		self.random_report_type(diagnostic_report)
		diagnostic_report.subject = FHIRReference({"reference":"urn:uuid:07f602e0-579e-4fe3-95af-381728bf0d49"}) #TODO find solution
		return diagnostic_report.as_json()

	def random_report_type(self, diagnostic_report):
		switcher={
		#	0:CompleteBloodCount(diagnostic_report),
			#1:HlaResult(diagnostic_report),
			0:LaboratoryReport(diagnostic_report),
			}
		return switcher.get(randrange(len(switcher))).next()




class CompleteBloodCount():
	def __init__(self, diagnostic_report, status = RandomStatus):
		self.diagnostic_report = diagnostic_report
		self.random_status = status		

	def next(self):
		self.diagnostic_report.code = self.__generate_code()

	def __generate_code(self):
	 	generate_codeable_concept = CodeableConcept()
	 	coding = Coding()
	 	coding.system =  "http://loinc.org" 
	 	coding.display = "Complete blood count (hemogram) panel - Blood by Automated count"
	 	coding.code =  "58410-2"
	 	list = [coding]
	 	generate_codeable_concept.coding = list 
	 	return generate_codeable_concept

	

class HlaResult():
	def __init__(self, diagnostic_report, status = RandomStatus):
		self.diagnostic_report = diagnostic_report
		self.random_status = status		

	def next(self):
		self.diagnostic_report.code = self.__generate_code()
		self.__set_meta()


	def __generate_code(self):
	 	generate_codeable_concept = CodeableConcept()
	 	coding = Coding()
	 	coding.system =  "http://loinc.org" 
	 	coding.display = "HLA-A+​B+​C (class I) [Type]"
	 	coding.code =  "13303-3"
	 	generate_codeable_concept.coding = [coding]
	 	return generate_codeable_concept

	def __set_meta(self):
		meta = Meta()
		meta.profile = ["http://hl7.org/fhir/StructureDefinition/hlaresult"]
		self.diagnostic_report.meta = meta




class LaboratoryReport():
	def __init__(self, diagnostic_report, status = RandomStatus):
		self.diagnostic_report = diagnostic_report
		self.random_status = status		

	def next(self):
		self.diagnostic_report.code = self.__generate_code()
		self.__set_meta()
		self.__set_category()
		self.__set_identifier()
		self.diagnostic_report.effectiveDateTime = RandomFHIRDates().next()
		self.diagnostic_report.issued = RandomFHIRDates().next()

	def __generate_code(self):
	 	generate_codeable_concept = CodeableConcept()
	 	coding = Coding()
	 	coding.system =  "http://loinc.org" 
	 	coding.display = "Laboratory report"
	 	coding.code =  "11502-2"
	 	generate_codeable_concept.coding = [coding]
	 	return generate_codeable_concept

	def __set_meta(self):
		meta = Meta()
		meta.profile = ["https://www.medizininformatik-initiative.de/fhir/core/modul-labor/StructureDefinition/DiagnosticReportLab"]
		self.diagnostic_report.meta = meta

	def __set_category(self):
		codeableconcept = CodeableConcept()
		coding_lab = Coding()
		coding_lab_studies = Coding()

		coding_lab.system = "http://terminology.hl7.org/CodeSystem/v2-0074"
		coding_lab.code = "LAB"
		coding_lab_studies.code =  "26436-6"
		coding_lab_studies.system = "http://loinc.org"
		coding_lab_studies.display = "Laboratory studies"

		codeableconcept.coding = [coding_lab, coding_lab_studies]
		self.diagnostic_report.category = [codeableconcept]

	def __set_identifier(self):
		identifier = Identifier()
		assigner_identifier = Identifier()
		coding = Coding()
		coding.system = "http://terminology.hl7.org/CodeSystem/v2-0203"
		coding.code = "FILL"
		codeableconcept = CodeableConcept()
		codeableconcept.coding = [coding]
		identifier.type = codeableconcept
		reference = FHIRReference({"identifier":{ "system": "https://www.medizininformatik-initiative.de/fhir/core/NamingSystem/org-identifier", "value": "DIZ-ID"}})

		# reference = FHIRReference({
  #         "system": "https://www.medizininformatik-initiative.de/fhir/core/NamingSystem/org-identifier"
		# })
		identifier.assigner = reference
		identifier.system = "https://diz.mii.de/fhir/core/NamingSystem/test-befund"
		identifier.value = "0987654321" # TODO randomize

		self.diagnostic_report.identifier = [identifier]

		return 



