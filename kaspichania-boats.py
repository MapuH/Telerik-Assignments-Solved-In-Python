"""Your task is to create the boats needed by the country of Kaspichania to win their next battle. You will be given the size of the desired bottom (N) of the boat and your task is to build it. The entire width of the boat must be N * 2 + 1 and the height: 6 + ((N - 3) / 2) * 3. The boats have sails with a height 2/3 of the entire height of the boat. The base of the boat is the other 1/3 of the height. The boats also have a supporting beam that goes through the entire height of the boat.

INPUT
The input data should be read from the console.
You have an integer number N - the size of the bottom of the boat.
The input data will always be valid and in the format described. There is no need to check it explicitly.

OUTPUT
The output should be printed on the console.
Use the "*" for the lines and "." (dot) for the rest."""

n = int(raw_input('Enter size of the bottom of the boat: '))
width = n * 2 + 1
height	= 6 + ((n - 3) / 2) * 3
base = list()

#top
sail = n * '.'
print sail + '*' + sail

#sail
sail = ['.' for x in range(n)]
for i in range(n - 1):
	sail[i] = '*'
	print ''.join(sail)[::-1] + '*' + ''.join(sail)
	base.append(''.join(sail)[::-1] + '*' + ''.join(sail))
	sail[i] = '.'

#middle
print '*' * width

#base
base.reverse()
for i in range((n-1)/2):
	print base[i]

#bottom
print '.' * ((n + 1)/2) + '*' * n + '.' * ((n + 1)/2)