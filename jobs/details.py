from lib import monthName

# ┌────────────────────────────────────────────────────────────
# │  The most important one
# │
# │  details every box at every month, showing remaining withdraws
# └──────────────────────────────────────────────────────────── 
def details(data):
	details_str = ''
	weights = {}

	# Get defined weights
	for box in data['boxes']:
		weights.update({box: data['boxes'][box]['weight']})

		


	# Get timeframes period and quantity wasted
	for timeframe in data['timeframes']:
		# period of time, available and remaining money
		period = timeframe['timeframe']
		available = timeframe['income'] * weight / 100
		wasted = timeframe['withdraws']['Wasted']
		rest = available - wasted

		# month name
		year, month = period.split('-')
		month_name = monthName(int(month))

		# tint quantity
		tint = ''
		if rest < (available / 10):
			tint = '\033[93m' # yellow
		if rest <= 0:
			tint = '\033[91m' # red
		if rest > (available / 2):
			tint = '\033[92m' # green

		# add line to the result array
		details_str += f'{period} ({month_name}): \t {wasted} / {available} \t = {tint} {rest} \033[0m \n' 
	
	return details_str


'''
2021-11 (Nov):	
	Indexa
	Finizens
	Personal
	Wasted
	Binance

'''