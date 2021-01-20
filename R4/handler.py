import randomizer
import json

slashes = 4


# TODO response ids are catched 2 times on time in the map functions and one time in the list generate functions, DUPLICATED!
def generate_id_list(response):
    lst = []
    for index in range(0, len(response["entry"])):
        lst.append(response["entry"][index]["resource"]["id"])
    return lst


def generate_seq_pat_map_bundle(response):
    for index in range(0, len(response["entry"])):
        seq_id = response["entry"][index]["resource"]["id"]
        # get patient ids
        pat_ids = response["entry"][index]["resource"]["patient"]["reference"].split("/")[1]
        randomizer.sequence_patient_map.append({"MolecularSequence/" + seq_id: "Patient/" + pat_ids})


def generate_obs_pat_map_bundle(response):
    for index in range(0, len(response["entry"])):
        obs_id = response["entry"][index]["resource"]["id"]
        pat_ids = response["entry"][index]["resource"]["subject"]["reference"].split("/")[1]
        randomizer.observation_patient_map.append({"Observation/" + obs_id: "Patient/" + pat_ids})


def patient_id_list_append(response):
    randomizer.patient_id_list.append(response["id"])


def diagnosticreport_id_list_append(response):
    randomizer.diagnosticreport_id_list.append(response["id"])


def observation_id_list_append(response):
    randomizer.observation_id_list.append(response["id"])


def sequence_id_list_append(response):
    randomizer.sequence_id_list.append(response["id"])


def generate_seq_pat_map_resource(response):
    seq_id = response["id"]
    # get patient ids
    pat_ids = response["patient"]["reference"].split("/")[1]
    randomizer.sequence_patient_map.append({"MolecularSequence/" + seq_id: "Patient/" + pat_ids})


def generate_obs_pat_map_resource(response):
    obs_id = response["id"]
    pat_ids = response["subject"]["reference"].split("/")[1]
    randomizer.observation_patient_map.append({"Observation/" + obs_id: "Patient/" + pat_ids})


def bundle_to_json(bundle):
    # print(json.dumps(bundle.bundle, ensure_ascii=False))
    return json.dumps(bundle.bundle, ensure_ascii=False)


def resource_to_json(resource):
    return json.dumps(resource, ensure_ascii=False)
