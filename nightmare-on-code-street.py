digits = raw_input('Enter digits: ')
digits = list(digits)
odd_digits = digits[1::2]
result = 0
for digit in odd_digits:
	result = result + int(digit)
print len(odd_digits), result