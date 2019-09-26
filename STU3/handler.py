import randomizer 
import json

def generate_id_list(response):
	lst = []
	for index in range(0, len(response["entry"])):
		lst.append(response["entry"][index]["resource"]["id"])
	return lst

def generate_seq_pat_map(response):
	for index in range(0, len(response["entry"])):
		seq_id = response["entry"][index]["resource"]["id"]
		# get patient ids
		pat_ids = response["entry"][index]["resource"]["patient"]["reference"].split("/")[4]	
		randomizer.sequence_patient_map.append({"Sequence/" + seq_id : "Patient/" +  pat_ids})

def generate_obs_pat_map(response):
	for index in range(0, len(response["entry"])):
		obs_id = response["entry"][index]["resource"]["id"]
		pat_ids = response["entry"][index]["resource"]["subject"]["reference"].split("/")[4]	
		randomizer.observation_patient_map.append({"Observation/" + obs_id : "Patient/" +  pat_ids})


def bundle_to_json(bundle):
	#print(json.dumps(bundle.bundle, ensure_ascii=False))
	return json.dumps(bundle.bundle, ensure_ascii=False)

