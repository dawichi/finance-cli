import json

# ┌────────────────────────────────────────────────────────────
# │  Returns the whole data formatted
# └──────────────────────────────────────────────────────────── 
def getFullData(data):
	return json.dumps(data, indent = 4, sort_keys=False)