# ┌────────────────────────────────────────────────────────────
# │  Returns the months registered (length of timeframes[])
# └──────────────────────────────────────────────────────────── 
def count(data):
	return 'Total months registered: ' + str(len(data['timeframes']))