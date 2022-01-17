import sys
import json

def loader():
	try:
		with open('./dta.json') as file:
			data = json.load(file)
		return data
	except FileNotFoundError:
		return None

sys.modules[__name__] = loader