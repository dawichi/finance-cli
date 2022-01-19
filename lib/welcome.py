import os
import sys
from lib import boolean_input

def welcome():
	os.system('cls' if os.name=='nt' else 'clear')
	print('''
┌───────────────────────────────────┐
│             FINANCE CLI           │
└───────────────────────────────────┘
   Hi! 😄 Welcome to Finance CLI!

We have not detected any 'box' in your system,
so we assume this is your first time here !

Would you like to go through the tutorial? ^^
-------
❌ Nah, I'm good, ty
✅ Yes! Let's do it!
-------
''')
	if boolean_input('Go to tutorial? (y/yes): '):
		print('cdsfasdsfd')

sys.modules[__name__] = welcome