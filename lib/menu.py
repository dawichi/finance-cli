import os
import sys

def menu(jobs):
	os.system('cls' if os.name=='nt' else 'clear')
	print('''
	┌───────────────────────────────────┐
	│             FINANCE CLI           │
	└───────────────────────────────────┘
	''')
	for index, job in enumerate(jobs):
		print(index, ': ', job["name"])
	print('---------------------------------')
	print()


sys.modules[__name__] = menu