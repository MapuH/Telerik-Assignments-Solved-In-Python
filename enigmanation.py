def solve_string (string):					#variable string is a list, function solves an equation w/o brackets
	while len(string) > 1:
		if string[1] == '+':
			result = int(string[0]) + int(string[2])
			string = string[3:]
			string.insert(0, str(result))
		elif string[1] == '-':
			result = int(string[0]) - int(string[2])
			string = string[3:]
			string.insert(0, str(result))
		elif string[1] == '%':
			result = int(string[0]) % int(string[2])
			string = string[3:]
			string.insert(0, str(result))
		elif string[1] == '*':
			result = int(string[0]) * int(string[2])
			string = string[3:]
			string.insert(0, str(result))
	return string[0]

riddle = raw_input('Enter the riddle: ')
riddle = riddle.rstrip('=')
riddle = list(riddle)

while '(' in riddle:
	open_bracket = []
	close_bracket = []
	brackets = []
	test =[]

	for i, j in enumerate(riddle):
		if j == '(':
			open_bracket.append(i)
		if j == ')':
			close_bracket.append(i)

	for i, j in zip(open_bracket, close_bracket):
		brackets.append(riddle[i+1:j])

	for i in range(open_bracket[0]):
		test.append(riddle[i])
	test.append(solve_string(brackets[0]))
	for i in range(close_bracket[0]+1,len(riddle)):
		test.append(riddle[i])
	riddle = test

print '%.3f' % float(solve_string(riddle))