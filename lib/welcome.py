import os
import sys

def welcome():
	os.system('cls' if os.name=='nt' else 'clear')
	print('''
┌───────────────────────────────────┐
│             FINANCE CLI           │
└───────────────────────────────────┘
   Hi! 😄 Welcome to Finance CLI!

We didn't have detected any stored file in your system,
so we assume this is your first time here !

Would you like to go through the tutorial? ^^
-------
❌ Nah, I'm good, ty
✅ Yes! Let's do it!
	''')
	print()


sys.modules[__name__] = welcome