import json
from lib import save


# ┌────────────────────────────────────────────────────────────
# │  Adds a new month structure (timeframe) 
# │
# │   {  timeframe: 'year-month',
# │	     income: xxxx
# │ 	 withdraws: [{ withdraw: xxxx }, ...]   }
# └──────────────────────────────────────────────────────────── 
def addMonth(data):
	DEFAULT_INCOME = 1600.00
	DEFAULT_MONTH = 1
	DEFAULT_YEAR = 2021

	# Get year-month from last timeframe and increment it
	try:
		year, month = data['timeframes'][-1]['timeframe'].split('-')
	except:
		# If there is no previous month saved, start point on Jan 2021
		year, month = DEFAULT_YEAR, DEFAULT_MONTH
		
	if (month == '12'):
		month = 1
		year = int(year) + 1
	else:
		month = int(month) + 1


	# Get income from this month
	valid = False
	while not valid:
		income = input(f'Income this month ({DEFAULT_INCOME}): ')
		if income == '':
			income = DEFAULT_INCOME
			valid = True
		else:
			try:
				income = float(income)
				valid = True
			except:
				print('That\'s not a valid input ;(')
	

	# get boxes and prepare withdraws object
	withdraws = {}
	for box in data['boxes']:
		withdraws.update({box: 0})

	for withdraw in withdraws:
		valid = False
		while not valid:
			quantity = input(f'Withdraw from {withdraw} (0): ')
			if quantity == '':
				quantity = 0
				valid = True
			else:
				try:
					withdraws[withdraw] = int(quantity)
					valid = True
				except:
					print('That\'s not a valid input ;(')


	# Add timeframe to the data and save it to the file
	timeframe_to_add = {
		"timeframe": f'{year}-{month}',
		"income": income,
		"withdraws": withdraws
	}
	data['timeframes'].append(timeframe_to_add)
	save.save(data)

	print(json.dumps(timeframe_to_add, indent = 4, sort_keys=False))
	return '\033[92mAdded successfully!\033[0m'