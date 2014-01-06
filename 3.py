>>> def prime(n):
	i = 2
	while (n%i != 0 and i < n):
		i += 1

	if (i < n):
		return prime(n/i)
	else:
		print ("Highest factor : "), n

		
>>> prime(600851475143)