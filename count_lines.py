'''

Aim: this script counts the number of lines in the standard input.
input: string from the command line.
output: counts the number of lines.
'''

import sys

count = 0
for line in sys.stdin:
	count+= 1

print(count, 'lines in standard input')
