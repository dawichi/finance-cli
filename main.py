# coding=utf-8

from jobs import jobs
from lib import loader, color, menu, welcome


# ┌────────────────────────────────────────────────────────────
# │  Main file of the program, where the magic ocurrs
# │
# │  runs the loop of the CLI to stay working
# └──────────────────────────────────────────────────────────── 
def run():
	# 1. Get data from file
	data = loader()
	# 2. If no data, create it!
	if data == None:
		welcome()
	return

	running = True
	while running:
		menu(jobs=jobs)
		answer = color.inputcolor(string='Execute: ', color="yellow")

		if answer.lower() == 'exit':
			running = False
			break

		try:
			option = int(answer)
			color.printcolor(string='--------------------', color="green")
			print(jobs[option]["func"](data))
			color.printcolor(string='--------------------', color="green")

		except ValueError:
			color.printcolor(string='That\'s not a number ;(', color="red")
			print('NOTE: You can quit by typing "exit"')

		except IndexError:
			color.printcolor(string='That\'s not a valid option ;(', color="red")

		color.inputcolor(string='Press ENTER to continue...', color='blue')


if __name__ == '__main__':
	# print(jobs[6]["func"](loader()))
	run()