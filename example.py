from threading import Thread
from duplex import Duplex
from time import sleep

def listener(inp):
	print(f'You said: {inp}')
	if inp == 'exit':
		print('Stopping :)')
		quit()

terminal = Duplex('> ')
print = terminal.print
terminal.listen(listener)
