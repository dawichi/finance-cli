import json

# Save JSON to a file
def save(data):
	with open('data.json', 'w') as outfile:
		json.dump(data, outfile, indent = 4, sort_keys=False)