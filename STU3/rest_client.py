from randomizer import * 
import requests
from handler import *
#CONFIG FILE MACHEN
base_url = 'Server_URL'

def main():
	post_patients(20)
	post_sequence(20)
	post_observation(20)
	post_diagnosticreport(20)

def post_patients(amount):
	bundle = random_patient_bundle(amount)
	response = post(bundle)
	print ("______Response Patient post:" + str(response))
	patient_ids = generate_id_list(response)
	init_patient_ids(patient_ids)

def post_sequence(amount):
	bundle = random_sequence_bundle(amount)
	response = post(bundle)
	print ("______Response Sequence post:" + str(response))
	sequence_ids = generate_id_list(response)
	init_sequence_ids(sequence_ids)
	generate_seq_pat_map(response)

def post_observation(amount):
	bundle = random_observation_bundle(amount)
	response = post(bundle)
	print ("______Response Observation post:" + str(response))
	observation_ids = generate_id_list(response)
	init_observation_ids(observation_ids)
	generate_obs_pat_map(response)

def post_diagnosticreport(amount):
	bundle = random_diagnosticreport_bundle(amount)
	response = post(bundle)
	print ("______Response DiagnosticReport post:" + str(response))
	diagnosticreport_ids = generate_id_list(response)
	init_diagnosticreport_ids(diagnosticreport_ids)

def post(data):
	header = {'Content-type': 'application/json', 'charset' : 'utf-8'}	
	#print (data)
	rsp = requests.post(base_url, data=data, headers=header)	
	return rsp.json()	

if __name__ == "__main__":
    main()
