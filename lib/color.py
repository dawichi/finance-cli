colors = {
	"purple": "\033[95m",
	"blue": "\033[94m",
	"cyan": "\033[96m",
	"green": "\033[92m",
	"yellow": "\033[93m",
	"red": "\033[91m",
	"gray": "\033[1m",
	"underline": "\033[4m",
	"end": "\033[0m",
}

def printcolor(string, color):
	return print(colors[color] + string + colors["end"])


def inputcolor(string, color):
	return input(colors[color] + string + colors["end"])


