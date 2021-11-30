from lib import monthName

# ┌────────────────────────────────────────────────────────────
# │  The most important one
# │
# │  details every box at every month, showing remaining withdraws
# └──────────────────────────────────────────────────────────── 
def details(data):

	wallet = {}

	# Added pending property to manage remaining deposits
	for box in data['boxes_definition']:
		wallet.update({
			box: {
				"weight": data['boxes_definition'][box]["weight"],
				"storage": data['boxes_definition'][box]["storage"],
				"pending": 0
			}
		})

	def pending(number):
		if number >= 100 and number < 199:
			return f'\033[93m{number}\033[0m'
		elif number >= 200:
			return f'\033[91m{number}\033[0m'
		else:
			return number

	def month_card(wallet, timeframe):
		month_name = monthName(int(timeframe["date"].split('-')[1]))
		result = f'\n  {timeframe["date"]} {month_name}: \t {timeframe["income"]}\n'
		result += '┌────────────────────────────────────────────────────────────────┐\n'
		result += '│ Box \t\tStorage \tExpected \tDone \tPending  │\n'
		result += '├────────────────────────────────────────────────────────────────┤\n'
		
		for box in wallet:
			storage = wallet[box]["storage"]
			expected = wallet[box]["weight"] * timeframe["income"] / 100
			deposit = timeframe['boxes'][box]['deposit']
			pending = expected - deposit
			tab1 = '\t' if len(str(storage)) > 6 else '\t\t'

			result += f'│ {box} \t{storage} {tab1}{expected} \t\t{deposit} \t{pending}\n'

		result += '└────────────────────────────────────────────────────────────────┘\n'
		print(result)


	# For each box...
	for timeframe in data['timeframes']:
		for box in timeframe['boxes']:
			# How much was thought for this month's deposit, and how much was done?
			expected_deposit = (data['boxes_definition'][box]['weight'] * timeframe['income'] / 100)
			deposit = timeframe['boxes'][box]['deposit']

			# Add the deposit done 
			wallet[box]['storage'] += deposit
			# Quit the withdraw
			wallet[box]['storage'] -= timeframe['boxes'][box]['withdraw']
			# Add the pending deposit
			wallet[box]['pending'] += expected_deposit - deposit
			# Round stuff
			wallet[box]['storage'] = round(wallet[box]['storage'], 1)
			wallet[box]['pending'] = round(wallet[box]['pending'], 1)
		month_card(wallet, timeframe)

	# development
	# return json.dumps(wallet['boxes_definition'], indent = 4, sort_keys=False)

	 

	# Build the result string
	total = 0
	result = ''
	result += '┌────────────────────────────────────────┐\n'
	result += '│ Box \t\tStorage \tPending  │\n'
	result += '├────────────────────────────────────────┤\n'
 
	for box in wallet:
		# Calc the total
		total += wallet[box]["storage"]
		# Tabulations for table display
		if len(str(wallet[box]["storage"])) > 6:
			tab2 = '\t'		
		else:
			tab2 = '\t\t'

		result += f'│ {box} \t{wallet[box]["storage"]} {tab2}{pending(wallet[box]["pending"])}\n'

	result += f'│ \n│ \ttotal:  \033[92m{total}\033[0m\n'
	result += '└────────────────────────────────────────┘\n'
	return result


'''
2021-11 (Nov):		856
	
	box				expctd	done	balance	
	----------------------------------
	Indexa (35):	299		300		expected-done			
	Finizens (25):	214		200
	Personal (20):	178		175
	Wasted (15):	150
	Binance (5):	47


2021-11 (Nov): 	856
┌────────────────────────────────────────┐
│ Box           Storage         Pending  	 │
├────────────────────────────────────────┤
│ Indexa C.     3000            299.6
│ Finizens      1000            214.0
│ Personal      977.8           171.2
│ Wasted        0               128.4
│ Binance       753.9           42.8
│ 
│       total:  5731.7
└────────────────────────────────────────┘
'''


