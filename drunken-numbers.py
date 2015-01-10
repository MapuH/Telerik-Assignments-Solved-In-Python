n = raw_input('Enter number of rounds: ')
rounds = int(n)
m_result = 0
v_result = 0
total = 0

for single_round in range(rounds):
	number = raw_input('Enter drunken number: ')
	if number[0] == '0':
		number = number.lstrip('0')
	if len(number) % 2 == 0:
		m_beers = number[:(len(number)/2)]
		v_beers = number[(len(number)/2):]
	elif len(number) == 1:
		m_beers = number
		v_beers = number
	else:
		m_beers = number[:((len(number)+1)/2)]
		v_beers = number[((len(number)-1)/2):]
	m_current = 0
	v_current = 0
	for digit in m_beers:
		m_current = m_current + int(digit)
	for digit in v_beers:
		v_current = v_current + int(digit)
	m_result = m_result + m_current
	v_result = v_result + v_current
	total = total + m_current + v_current

if m_result == v_result:
	print 'No', total
elif m_result > v_result:
	print 'M', m_result - v_result
else:
	print 'v', v_result - m_result
