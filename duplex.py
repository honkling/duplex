from re import sub
from sys import stdout
from readline import get_line_buffer
from time import sleep

class Duplex:
	def __init__(self, prefix: str = '> '):
		self.ERASE = '\x1b[2K'
		if type(prefix) != str:
			received_type = sub('(<class\ \'|\'>)', '', str(type(text)))
			raise TypeError(f'Expected type \'str\', received type \'{received_type}\'')
		self.prefix = f'\n{prefix}'
	
	def print(self, text: str = ''):
		if text == '':
			raise Exception('Text must not be empty.')
		elif type(text) != str:
			received_type = sub('(<class\ \'|\'>)', '', str(type(text)))
			raise TypeError(f'Expected type \'str\', received type \'{received_type}\'')
		inp = get_line_buffer()
		stdout.write(self.ERASE)
		print(f'\r{text}{self.prefix}{inp}', end='')
	
	def listen(self, listener):
		if callable(listener) == False:
			raise Exception(f'Listener must be callable.')
		print(self.prefix, end='')
		inp = ''
		while inp == '':
			try:
				inp = input()
				listener(inp)
				inp = ''
			except KeyboardInterrupt:
				break