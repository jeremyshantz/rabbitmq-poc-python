import sys
import os

def test(message):
	f = open(os.path.expanduser('~/') + 'dev/portfolio-sim/output.txt', mode = 'at', encoding = 'utf-8' )
	f.write(message + '\n')
	f.close()

test('hello')