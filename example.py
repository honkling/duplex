from threading import Thread
from duplex import Duplex
from time import sleep

def listener(inp):
	print(f'You said: {inp}')
	if inp == 'exit':
		print('Stopping :)')
		quit()

def send():
	while True:
		print('epic message')
		sleep(1)

thread = Thread(target=send)
thread.daemon = True
thread.start()

terminal = Duplex('> ')
print = terminal.print
terminal.listen(listener)