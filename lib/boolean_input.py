import sys
def boolean_input(text):
	return input(text).lower() in ['y', 'yes']


sys.modules[__name__] = boolean_input