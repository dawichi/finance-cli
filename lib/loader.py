import sys
import json

def loader():
	with open('./data.json') as file:
		data = json.load(file)
	return data

sys.modules[__name__] = loader