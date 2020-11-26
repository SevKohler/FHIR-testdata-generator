class Fhir_object_generator ():

    def write_output_file(self, fhir_sequence, file_name):
        with open("out/"+file_name, 'w') as f:
            print(fhir_sequence, end="", file=f)


class Fhir_object:
    # resourceType = ""
    # id = 0

    def __init__(self, id, resourceType):
        self.id = id
        self.resourceType = resourceType
        self.url = resourceType + "/"

class Patient (Fhir_object):
    def __init__(self, id, active, first_name, last_name, gender, birthDate, deceasedBoolean):
        self.active = active
        self.name = {"family": first_name, "given": [last_name]}
        self.gender = gender
        self.birthDate = birthDate
        self.deceasedBoolean = deceasedBoolean
        super(Patient, self).__init__(id, 'Patient')

    def as_dict(self):
        return {
 #               "id" : self.id,
                "resourceType" : self.resourceType,
                "active" : self.active,
                "name" : self.name,
                "gender" : self.gender,
                "birthDate" : self.birthDate,
                "deceasedBoolean" : self.deceasedBoolean
                }

class Diagnostics (Fhir_object):
    status = ""
    code = {}
    subject = {"reference" : None}

    def __init__(self, id, resourceType, status, code, subject):
        self.status = status
        self.code = code
        self.subject["reference"] = subject
        super(Diagnostics, self).__init__(id, resourceType)


class MolecularSequence (Fhir_object):
    referenceSeq = {}
    variant = [{}]
    patient = {"reference" : None}


    def __init__(self, id, type, coordinate_system, patient, referenceSeq, variant):
       self.type = type
       self.coordinate_system = coordinate_system
       #self.patient = patient
       self.patient["reference"] = patient

       self.referenceSeq["chromosome"] = referenceSeq["chromosome"]
       self.referenceSeq["genomeBuild"] = "GRCh 37"
       self.referenceSeq["windowStart"] = referenceSeq["windowStart"]
       self.referenceSeq["windowEnd"] = referenceSeq["windowEnd"]
        #possiblity for mutltiple variants exists therefor we work here with an index of 0
       self.variant[0]["start"] = variant[0]["start"] 
       self.variant[0]["end"] = variant[0]["end"] 
       self.variant[0]["observedAllele"] = variant[0]["observedAllele"] 
       self.variant[0]["cigar"] = variant[0]["cigar"] 
      # self.variant[0]["variantPointer"] = variant[0]["variantPointer"] 
       super(MolecularSequence, self).__init__(id, "MolecularSequence")

    def as_dict(self):  
        return {  
    #            "id" : self.id,   
                "resourceType" : self.resourceType,    
                "type" : self.type, 
                "coordinateSystem" : self.coordinate_system, 
                "patient" : self.patient,    
                "referenceSeq" : self.referenceSeq, 
                "variant" : self.variant 
                }

# class DiagnosticReport (Diagnostics):
#     result = [{}]
#  #   conclusionCode = [{}]

#     def __init__(self, id, status, code, subject, result):
#         self.result[0] = {"reference" : result}
#         #  self.conclusionCode = conclusionCode
#         super(DiagnosticReport, self).__init__(id, "DiagnosticReport", status, code, subject)

#     def as_dict(self):
#         return {
#         #        "id" : self.id,
#                 "resourceType" : self.resourceType,
#                 "status" : self.status,
#                 "code" : self.code,
#                 "subject" : self.subject,
#                 "result" : self.result
#                 }

# class Observation (Diagnostics):
#     derivedFrom = {}

#     def __init__(self, id, status, code, subject, derivedFrom):
#         self.derivedFrom["reference"] = derivedFrom
#         super(Observation, self).__init__(
#             id, "Observation", status, code, subject)

#     def as_dict(self):
#             return {
#         #        "id" : self.id,
#                 "resourceType" : self.resourceType,
#                 "status" : self.status,
#                 "code" : self.code,
#                 "subject" : self.subject,
#                 "derivedFrom" : self.derivedFrom
#                 }


class Bundle():
    def __init__(self):
        self.bundle = {"resourceType" : "Bundle", "type" : "transaction", "entry" : []}

    def add_element(self, element):
        # URL of resource       
        element = self.parse_entry_format(element)
        self.bundle["entry"].append(element)

    def parse_entry_format(self, element):
        request = { "method" : "POST", "url":  element.url}
        element = {"resource" : element.as_dict(), "request" : request}
        return element
#json.dumps(your_data, ensure_ascii=False)
   # def to_string(self):

# if __name__ == "__main__":
#     main()
