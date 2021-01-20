# -*- coding: utf-8 -*-
from R4.randomizer.randomizer import *
import requests
from R4.generators.diagnostic_report_generator import *
from R4.handler import *

base_url = "http://localhost:8888/fhir-bridge/fhir/"
username = "myuser"
password = "myPassword432"


def main():
    diagnostic_report_generator = DiagnosticReportGenerator()

    post(diagnostic_report_generator.next(), "DiagnosticReport")
    # for index in range(0, 1):  # Enter amount\
    #     diagnostic_report_generator = DiagnosticReportGenerator()
    #
    #     post(diagnostic_report_generator.next(), "DiagnosticReport")
    # post_patient_resource()
    # post_sequence_resource()
    # post_observation_resource()
    # post_diagnosticreport_resource()


# Post as BUNDLES !!!! (not yet supported by some FHIR R4 providers)
# post_patient_bundle(20)
# post_sequence_bundle(20)
# post_observation_bundle(20)
# post_diagnosticreport_bundle(20)

def post_patient_bundle(amount):
    bundle = random_patient_bundle(amount)
    response = post(bundle)
    print("______Response Patient post:" + str(response))
    patient_ids = generate_id_list(response)
    init_patient_ids(patient_ids)


def post_observation_bundle(amount):
    bundle = random_observation_bundle(amount)
    response = post(bundle)
    print("______Response Observation post:" + str(response))
    observation_ids = generate_id_list(response)
    init_observation_ids(observation_ids)
    generate_obs_pat_map_bundle(response)


def post_sequence_bundle(amount):
    bundle = random_sequence_bundle(amount)
    response = post(bundle)
    print("______Response Sequence post:" + str(response))
    sequence_ids = generate_id_list(response)
    init_sequence_ids(sequence_ids)
    generate_seq_pat_map_bundle(response)



def post_diagnosticreport_bundle(amount):
    bundle = random_diagnosticreport_bundle(amount)
    response = post(bundle)
    print("______Response DiagnosticReport post:" + str(response))
    diagnosticreport_ids = generate_id_list(response)
  #  init_diagnosticreport_ids_bundle(diagnosticreport_ids)


# --------------Single resources ---------------

# def post_patient_resource():
#     resource = resource_to_json(RandomPatient().generate_patient().as_dict())
#     response = post(resource, "Patient")
#     print("______Response Patient post:" + str(response))
#     patient_id_list_append(response)

#
# def post_sequence_resource():
#     resource = resource_to_json(RandomMolecularSequence().generate_sequence().as_dict())
#     response = post(resource, "MolecularSequence")
#     print("______Response Sequence post:" + str(response))
#     sequence_id_list_append(response)
#     generate_seq_pat_map_resource(response)
#
#
# def post_observation_resource():
#     resource = resource = resource_to_json(RandomObservation().generate_observation().as_dict())
#     response = post(resource, "Observation")
#     print("______Response Observation post:" + str(response))
#     observation_id_list_append(response)
#     generate_obs_pat_map_resource(response)
#
#
# def post_diagnosticreport_resource():
#     resource = resource_to_json(RandomDiagnosticReport().generate_report().as_dict())
#     response = post(resource, "DiagnosticReport")
#     print("______Response DiagnosticReport post:" + str(response))
#     diagnosticreport_id_list_append(response)


# def post(data, resource_name=""):
# 	header = {'Content-type': 'application/fhir+json; fhirVersion=4.0', 'Accept':'application/fhir+json; fhirVersion=4.0', 'charset' : 'utf-8'}	
# 	rsp = requests.post(base_url+resource_name, data=data.encode("utf-8"), headers=header)	
# 	return rsp.json()

def post(data, resource_name=""):
    print(json.dumps(data, sort_keys=True, indent=4))
    header = {'Content-Type': 'application/json'}
    print(base_url + resource_name)
    rsp = requests.post(base_url + resource_name, data=data, headers=header, auth=(username, password))
    print(json.dumps(rsp.json(), sort_keys=True, indent=4))


if __name__ == "__main__":
    main()
