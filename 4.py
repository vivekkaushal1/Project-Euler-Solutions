>>> def chckPalin(num):
	return str(num) == str(num)[::-1]

>>> def fun(n):
		maxval = 1
		for x in range(n, 1, -1):
			for y in range(n, x-1, -1):
				if (chckPalin(x*y) and x*y > maxval):
					maxval = x*y
				elif x*y < maxval:
					break
		return maxval

	
>>> print fun(999)