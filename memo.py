
for n in range(20):
	answer = ''
	while n != 0:
		n, p = map(int, divmod(n, 3))
		if p == 1:
			answer = answer + '1'
		if p == 2:
			answer = answer + '2'
		if p == 0:
			answer = answer + '4'
	answer = answer[::-1]
	print(answer)
 
