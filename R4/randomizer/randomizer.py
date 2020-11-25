from random import *
import json
from classes import *
import sys
from  handler import *
from fhir.resources.fhirdate import FHIRDate


#TODO !!! throw error if empty 
patient_id_list = []
diagnosticreport_id_list = []
observation_id_list = []
sequence_id_list = []

# Map with key value pairs of ids
observation_patient_map = []
report_patient_map = []
sequence_patient_map = []

# References has to be fixed ! Functionality scattered all over the script...

#tests
# def main():
# 	#data = random_value_bundle(30)
# 	bundle = random_patient_bundle()
# 	bundle_to_json(bundle)

#Sinnvoll da eh global ???
# SOLLTE EIGENTLICH IN DEN HANDLER ? 
def init_patient_ids(patient_ids):
	global patient_id_list
	patient_id_list = patient_ids

def init_sequence_ids(seq_ids):
	global sequence_id_list
	sequence_id_list = seq_ids  

def init_observation_ids(observation_ids):
	global observation_id_list
	observation_id_list = observation_ids  

def init_diagnosticreport_ids(dr_ids):
	global diagnosticreport_id_list
	diagnosticreport_id_list = dr_ids

def init_sequence_patient_map(seq_pat_map):
	global sequence_patient_map
	sequence_patient_map = seq_pat_map  




# def init_sequence_patient_map(seq_pat_map):
# 	global sequence_patient_map
# 	sequence_patient_map = seq_pat_map  

#in Handler verlegen 
def load_json_file(filename):
	data = None
	with open('../resources/'+filename) as f:
		data = json.load(f)
	return data


def random_patient_bundle(amount):
	random_patients = RandomPatient()
	bundle = Bundle()
	for x in range(0,amount):
		bundle.add_element(random_patients.generate_patient())	
	return bundle_to_json(bundle)

def random_sequence_bundle(amount):
	random_sequence = RandomMolecularSequence()
	bundle = Bundle()
	for x in range(0,amount):
		bundle.add_element(random_sequence.generate_sequence())	
	return bundle_to_json(bundle)

def random_observation_bundle(amount):
	random_observation = RandomObservation()
	bundle = Bundle()
	for x in range(0,amount):
		bundle.add_element(random_observation.generate_observation())	
	return bundle_to_json(bundle)

def random_diagnosticreport_bundle(amount):
	random_diagnosticreport = RandomDiagnosticReport()
	bundle = Bundle()
	for x in range(0,amount):
		bundle.add_element(random_diagnosticreport.generate_report())	
	return bundle_to_json(bundle)

def random_dict_list_items(dict_list):
	random_index = choice(dict_list)
	value_pair = list(random_index.items())
	return value_pair[0][0], value_pair[0][1]

class RandomNames:
	def __init__(self):
		self.names = load_json_file('names.json')

	def next(self):
		return self.names[randrange(len(self.names))]

class RandomFirstNames:
	def __init__(self):
		self.first_names = load_json_file('first_names.json')
	
	def next(self):
		return self.first_names[randrange(len(self.first_names))]

class RandomGenders:
	def __init__(self):
		self.genders = load_json_file('genders.json')

	def next(self):
		return self.genders[randrange(len(self.genders))]

class RandomDates:
	def next(self):
		#return "{}-{}-{}".format(randint(1, 27), randint(1, 12), randint(1900, 2019))
		day = self.random_day()
		month = self.random_month()
		return "{}-{}-{}".format(randint(1915, 2019), month, day)

	def random_month(self):
		return self.add_leading_zero(str(randint(1, 12)))

	def random_day(self):
		return self.add_leading_zero(str(randint(1, 27)))

	def add_leading_zero(self, digit):
		if (len(digit)<=1):
			digit = "0" + digit
		return digit

class RandomFHIRDates:
	def next(self):
		#return "{}-{}-{}".format(randint(1, 27), randint(1, 12), randint(1900, 2019))
		day = self.random_day()
		month = self.random_month()
		hour = self.random_hour()
		minute = self.random_minute()
		second = self.random_second()
		algebraic_sign = self.random_algebraic_sign()
		addition = self.random_addition()
		date = "{}-{}-{}T{}:{}:{}{}{}:00".format(randint(1915, 2019), month, day, hour, minute, second, algebraic_sign, addition)
		return FHIRDate(date)

	def random_month(self):
		return self.add_leading_zero(str(randint(1, 12)))

	def random_day(self):
		return self.add_leading_zero(str(randint(1, 29)))

	def random_hour(self):
		return self.add_leading_zero(str(randint(1, 24)))

	def random_minute(self):
		return self.add_leading_zero(str(randint(1, 59)))

	def random_second(self):
		return self.add_leading_zero(str(randint(1, 59)))

	def random_algebraic_sign(self):
		switcher={0:"+", 1:"-"}
		return switcher.get(randrange(len(switcher)))

	def random_addition(self):
		return self.add_leading_zero(str(randint(1, 7)))

	def add_leading_zero(self, digit):
		if (len(digit)<=1):
			digit = "0" + digit
		return digit


class RandomBooleans:
	def next(self):
		return bool(getrandbits(1))

class RandomLoinc:
	def __init__(self):
		self.loinc = load_json_file('loinc.json')
	#Returns only code but can also return text if needed ["text"]
	def next(self):
		return {"coding" : [{"code" : self.loinc["loinc"][randrange(len(self.loinc["loinc"]))]["code"] }]}


class RandomNumber:
	def next(self):
		return randrange(10)

class RandomPatientId:
	def next(self):
		return  "Patient/"+str(choice(patient_id_list))

class RandomSequenceType:
	def next(self):
		sequence_type = ("dna","rna")
		return sequence_type[randrange(len(sequence_type))]
		
class RandomStatus:
	def next(self):
		status_list = (	"registered" , "preliminary" , "final" , "amended" )
		return choice(status_list)

class RandomReferenceSequence:
	def __init__(self):
		self.chromosome = load_json_file('chromosomes.json')
		self.chromosome = self.chromosome["chromosomes"]

	def next(self):
		referenceSeq = {}
		index = randrange(len(self.chromosome))
		code = {"coding" : [{"code" : self.chromosome[index]["code"]}]}
		#code =  self.chromosome[index]["code"]
		windowStart = randrange(self.chromosome[index]["length"]-1)
		windowEnd = randrange(windowStart+1, self.chromosome[index]["length"])
		referenceSeq["chromosome"] = code
		referenceSeq["windowStart"] = windowStart
		referenceSeq["windowEnd"] = windowEnd
		return referenceSeq

class RandomVariant:
	def next(self):
		variant = [{}]
		start = randrange(248756544-1)
		end = randrange(start + 1, start+10)
		variant[0]["start"] = start
		variant[0]["end"] = end
		variant[0]["observedAllele"] = self.random_allele(end-start)
		variant[0]["cigar"] = "None" # due to lack of example data
		variant[0]["variantPointer"] = "None" # would need an observation but the observation also needs a sequence -> paradox
		return variant

	def random_allele(self, length):
		bases = ("A", "G", "T", "C")
		allele = ""
		for x in range (0, length):
			allele += bases[randrange(len(bases))]
		return allele


#-------- Core Factories ------------
# Spaghetti code abstraction into one mother class would be useful
# spliot maybe into one ramonizer class which can generate what is needed.

# class RandomPatient: 
# 	def __init__(self, names = RandomNames(), first_names = RandomFirstNames(), genders = RandomGenders(), dates = RandomDates(), booleans = RandomBooleans()):
# 		self.random_names = names
# 		self.random_first_names = first_names
# 		self.random_genders = genders
# 		self.random_dates = dates
# 		self.random_booleans = booleans

# 	def generate_patient(self):
# 	#	id = idGenerator.next_patient()
# 		id = 1
# 		name = self.random_names.next()
# 		first_name= self.random_first_names.next()
# 		gender = self.random_genders.next()
# 		birth_date = self.random_dates.next()
# 		status = self.random_booleans.next()
# 		deceased = self.random_booleans.next()
# 		patient = Patient(id, status, first_name, name, gender, birth_date , deceased)
# 		return patient


# class RandomDiagnosticReport:
# 	def __init__(self, loinc_codes = RandomLoinc(), booleans = RandomBooleans(), status = RandomStatus()):
# 		self.random_booleans = booleans
# 		self.random_loinc = loinc_codes
# 		self.random_status = status

# 	def generate_report(self):
# 		global report_patient_map
# 		#id = idGenerator.next_diagnosticreport()
# 		id = 1
# 		result, subject =random_dict_list_items(observation_patient_map)
# 		status = self.random_status.next()
# 		code = self.random_loinc.next()
# 		diagnostic_report = DiagnosticReport (id, status, code, subject, result)
# 		return diagnostic_report

# class RandomObservation:
# 	def __init__(self, loinc_codes = RandomLoinc(), status = RandomStatus(), patient_id = RandomPatientId()):
# 		self.random_status = status
# 		self.random_loinc = loinc_codes
# 		self.patient_id = patient_id

# 	def generate_observation(self):
# 		global observation_patient_map
# 		#id = idGenerator.next_observation()
# 		id = 1
# 		# ugly split into more methods ?
# 		#if(randint(0,1)==0):
# 		derivedFrom, subject = random_dict_list_items(sequence_patient_map)
# 		# else:
# 		# 	related, subject = self.generate_empty_related()
# 		#observation_patient_map["Observation/"+str(id)] = subject
# 		status = self.random_status.next()
# 		code = self.random_loinc.next()
# 		observation = Observation (id, status, code, subject, derivedFrom)
# 		return observation

# 	# def generate_empty_related(self):
# 	# 	return None, self.patient_id.next()

# class RandomMolecularSequence:
# 	def __init__(self, patient_id = RandomPatientId(), sequence_type = RandomSequenceType(), reference_sequence = RandomReferenceSequence(), variant = RandomVariant()):
# 		self.patient_id = patient_id
# 		self.sequence_type = sequence_type
# 		self.reference_sequence = reference_sequence
# 		self.variant = variant

# 	def generate_sequence(self):
# 	#	id = idGenerator.next_sequence()
# 		id = 1
# 		patient = self.patient_id.next()
# 		coordinateSystem = randrange(0,1)
# 		sequence_type = self.sequence_type.next()
# 		reference_sequence = self.reference_sequence.next()
# 		variant = self.variant.next()
# 		sequence = MolecularSequence (id, sequence_type, coordinateSystem, patient, reference_sequence, variant) #default DNA 
# 		return sequence

# if __name__ == "__main__":
#     main()
