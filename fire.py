width = int(raw_input('Enter width of the fire: '))

for i in range(width / 2):
	string = list('.' * (width / 2))
	string[i] = '#'
	line = ''.join(string)
	print line[::-1] + line

for i in range(width / 4):
	string = list('.' * (width / 2))
	string[i] = '#'
	line = ''.join(string)
	print line + line[::-1]

print '-' * width
print ('\\' * (width / 2)) + ('/' * (width / 2))

lstring = list('\\' * (width / 2))
rstring = list('/' * (width / 2))

for i in range(width / 2 - 1):
	lstring[i] = '.'
	rstring[i] = '.'
	lline = ''.join(lstring)
	rline = ''.join(rstring)
	rline = rline[::-1]
	print lline + rline