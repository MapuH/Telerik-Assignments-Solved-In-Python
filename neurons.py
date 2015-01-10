def convert_raw(raw):
	first1 = raw.find('1')
	last1 = 31 - raw[::-1].find('1')
	extract = raw[first1:last1+1]
	extract_rev = list()

	for i in extract:
		if i == '1':
			extract_rev.append('0')
		else:
			extract_rev.append('1')

	extract_rev = ''.join(extract_rev)
	raw = raw[:first1] + extract_rev + raw[last1+1:]
	return raw

numbers = list()
while True:
	integer = int(raw_input('Enter an integer: '))
	if integer == -1:
		break
	else:
		numbers.append(integer)

#test list
"""numbers = [480, 272, 224, 16252928, 50593792, 33685504, 67239936, 67174400, 33587200, 16809984, 16973824, 8650752, 7864320, 0]"""
binaries = []

#graphic input
for number in numbers:
	print format(number, '032b')

print "\n"

#graphic output
for number in numbers:
	if '1' in format(number, '032b'):
		print convert_raw(format(number, '032b'))
		binaries.append('0b' + convert_raw(format(number, '032b')))
	else:
		print format(number, '032b')
		binaries.append('0b' + format(number, '032b'))

print "\n"

for binary in binaries:
	print int(binary, 2)