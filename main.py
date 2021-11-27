from jobs import jobs
from lib import loader, color, init


# ┌────────────────────────────────────────────────────────────
# │  Main file of the program, where the magic ocurrs
# │
# │  runs the loop of the CLI to stay working
# └──────────────────────────────────────────────────────────── 
def run():
	data = loader()
	running = True
	while running:
		init(jobs=jobs)
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
	# print(jobs[1]["func"](loader()))
	run()