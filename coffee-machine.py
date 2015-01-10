n1 = raw_input('Enter N1: ')
n2 = raw_input('Enter N2: ')
n3 = raw_input('Enter N3: ')
n4 = raw_input('Enter N4: ')
n5 = raw_input('Enter N5: ')
a = raw_input('Enter amount: ')
p = raw_input('Enter price: ')

total = 0.05 * int(n1) + 0.10 * int(n2) + 0.20 * int(n3) + 0.50 * int(n4) + 1.00 * int(n5)

if float(p) > float(a):
	nedostig = float(p) - float(a)
	print 'More %.2f' % nedostig
elif total >= float(a) - float(p):
	left = total - (float(a) - float(p))
	print 'Yes %.2f' % left
else:
	insufficient = float(a) - float(p) - total
	print 'No %.2f' % insufficient