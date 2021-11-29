from lib import monthName

# ┌────────────────────────────────────────────────────────────
# │  JOB only available with a 'wasted' box active 
# │
# │  checks if each month you messed it up any 
# └──────────────────────────────────────────────────────────── 
def wasted(data):
	wasted_by_month = ''
	global weight

	# Get wasted weight
	for box in data['boxes']:
		if box == 'Wasted':
			weight = data['boxes'][box]['weight']


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
		wasted_by_month += f'{period} ({month_name}): \t {wasted} / {available} \t = {tint} {rest} \033[0m \n' 
	
	return wasted_by_month
