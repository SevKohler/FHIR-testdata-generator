from random import randrange

from R4.randomizer.randomizer import load_json_file


class RandomLoinc:
	def __init__(self):
		self.loinc = load_json_file('loinc.json')
	#Returns only code but can also return text if needed ["text"]
	def next(self):
		return {"coding" : [{"code" : self.loinc["loinc"][randrange(len(self.loinc["loinc"]))]["code"] }]}
