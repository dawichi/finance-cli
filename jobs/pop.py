import json
from lib import save

# ┌────────────────────────────────────────────────────────────
# │  Asks booleanly if delete the last item in timeframes[]
# └──────────────────────────────────────────────────────────── 
def pop(data):
	print(json.dumps(data['timeframes'][-1], indent = 4, sort_keys=False))
	print('---------------------------------')
	print('Are you sure you wanna delete this item?')
	print('This action can\'t be undone !')
	confirm = input('Delete? (yes/no): ')

	if confirm.lower() == 'yes' or confirm.lower() == 'y':
		data['timeframes'].pop()
		save.save(data)
		return 'Item deleted.'
	else:
		return 'Aborted.'