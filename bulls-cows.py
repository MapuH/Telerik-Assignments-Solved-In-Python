number = raw_input('Enter secret number: ')
bulls = int(raw_input('Bulls: '))
cows = int(raw_input('Cows: '))
orig_value = number

if int(bulls) + int(cows) > 4:
	print 'No'
	quit()
if int(bulls) == 3 and int(cows) == 1:
	print 'No'
	quit()

all_guesses = [x for x in range(1111, 10000) if '0' not in str(x)]

for guess in all_guesses:
	number = orig_value
	num_bulls = 0
	num_cows = 0
	guess = str(guess)
	for i, j in zip(guess, number):
		if i == j:
			num_bulls = num_bulls + 1
	for i in guess:
		if i in number:
			num_cows = num_cows + 1
			number = number.replace(i, '', 1)
	num_cows = num_cows - num_bulls
	if num_bulls == bulls and num_cows == cows:
		print guess,