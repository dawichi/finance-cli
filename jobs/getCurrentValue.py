# ┌────────────────────────────────────────────────────────────
# │  Gets the total value of the Boxes
# │
# │  prints the values by box and in total 
# └──────────────────────────────────────────────────────────── 
import json
def getCurrentValue(data):

	# Added pending property to manage remaining deposits
	for box in data['boxes_definition']:
		data['boxes_definition'][box].update({"pending": 0})

	# For each box...
	for timeframe in data['timeframes']:
		for box in timeframe['boxes']:
			# How much was thought for this month's deposit, and how much was done?
			expected_deposit = (data['boxes_definition'][box]['weight'] * timeframe['income'] / 100)
			deposit = timeframe['boxes'][box]['deposit']

			# Add the deposit done 
			data['boxes_definition'][box]['storage'] += deposit
			# Quit the withdraw
			data['boxes_definition'][box]['storage'] -= timeframe['boxes'][box]['withdraw']
			# Add the pending deposit
			data['boxes_definition'][box]['pending'] += expected_deposit - deposit
			# Round stuff
			data['boxes_definition'][box]['storage'] = round(data['boxes_definition'][box]['storage'], 1)
			data['boxes_definition'][box]['pending'] = round(data['boxes_definition'][box]['pending'], 1)
	
	# development
	# return json.dumps(wallet, indent = 4, sort_keys=False)


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
 
	for box in data['boxes_definition']:
		# Calc the total
		total += data['boxes_definition'][box]["storage"]
		# Tabulations for table display
		if len(str(data['boxes_definition'][box]["storage"])) > 6:
			tab2 = '\t'		
		else:
			tab2 = '\t\t'

		result += f'│ {box} \t{data["boxes_definition"][box]["storage"]} {tab2}{pending(data["boxes_definition"][box]["pending"])}\n'

	result += f'│ \n│ \ttotal:  \033[92m{total}\033[0m\n'
	result += '└────────────────────────────────────────┘\n'
	return result