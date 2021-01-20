from fhir.resources.diagnosticreport import *
from fhir.resources.codeableconcept import CodeableConcept
from fhir.resources.coding import Coding
from fhir.resources.reference import Reference
from fhir.resources.identifier import Identifier
from fhir.resources.observation import Observation

from R4.randomizer.randomizer import *
from R4.generators.generator import Generator


class ObservationGenerator():
    def __init__(self):
        pass

    def next(self):
        pass


class ObservationLabGenerator(Generator):

    def __init__(self):
        self.observation = Observation.construct()
        self.url = "https://www.medizininformatik-initiative.de/fhir/core/modul-labor/StructureDefinition/ObservationLab"

    def next(self):
        Generator.set_status(self, self.observation)
        Generator.set_meta(self, self.url, self.observation)
        self.__set_identifier()
        self.__set_category()
        self.__generate_code()
        return self.observation

    def __set_identifier(self):
        identifier = Identifier()
        assigner_identifier = Identifier()
        coding = Coding()
        coding.system = "http://terminology.hl7.org/CodeSystem/v2-0203"  # fixed
        coding.code = "OBI"  # fixed
        generate_codeable_concept = CodeableConcept()
        generate_codeable_concept.coding = [coding]
        identifier.type = generate_codeable_concept
        reference = Reference.parse_obj({"identifier": {
            "system": "https://www.medizininformatik-initiative.de/fhir/core/NamingSystem/org-identifier",
            "value": "DIZ-ID"}})
        identifier.assigner = reference
        identifier.system = "https://diz.mii.de/fhir/core/NamingSystem/test-lab-results"
        identifier.value = "59826-8_1234567890"  # TODO randomize
        self.observation.identifier = [identifier]

    def __set_category(self):
        codeableconcept = CodeableConcept()
        coding_lab = Coding()
        coding_loinc = Coding()
        coding_lab.system = "http://terminology.hl7.org/CodeSystem/observation-category"
        coding_lab.code = "laboratory"
        coding_loinc.system = "http://loinc.org"
        coding_loinc.code = "26436-6"
        codeableconcept.coding = [coding_lab, coding_loinc]
        self.observation.category = [codeableconcept]

    def __generate_code(self):
        codeable_concept = CodeableConcept()
        coding = Coding()
        coding.system = "http://loinc.org"
        coding.display = "Lymphocytes [#/volume] in Blood by Manual count"
        coding.code = "732-8"
        codeable_concept.coding = [coding]
        self.observation.code = codeable_concept
