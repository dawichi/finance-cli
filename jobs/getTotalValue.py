def getTotalValue(data):
	total = 0
	wallet = {}
	weights = {}

	# Get initial value from boxes
	for box in data['boxes']:
		total += data['boxes'][box]['storage']
		wallet.update({box: data['boxes'][box]['storage']})
		weights.update({box: data['boxes'][box]['weight']})

	
	# Apply calculated cuantity from each month to each box
	for timeframe in data['timeframes']:
		total += timeframe['income']
		
		for withdraw in timeframe['withdraws']:
			total -= int(timeframe['withdraws'][withdraw])
			wallet[withdraw] -= timeframe['withdraws'][withdraw]
		
		for weight in weights:
			wallet[weight] += timeframe['income'] * weights[weight] / 100


	# Build the result string to print
	result = ''
	for box in wallet:
		if wallet[box] <= 0:
			wallet[box] = f'\033[91m{wallet[box]}\033[0m'
		result += f'\033[96m{box}\033[0m: \t {wallet[box]} \n'
	result += '--------------------\n'
	result += f'total: \t\t {total}'

	return result