# ┌────────────────────────────────────────────────────────────
# │  Gets the total value of the Boxes
# │
# │  prints the values by box and in total 
# └──────────────────────────────────────────────────────────── 
import json
def getCurrentValue(data):

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
	
	# development
	# return json.dumps(wallet['boxes_definition'], indent = 4, sort_keys=False)


	def pending(number):
		if number >= 100 and number < 199:
			return f'\033[93m{number}\033[0m'
		elif number >= 200:
			return f'\033[91m{number}\033[0m'
		else:
			return number
	 

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