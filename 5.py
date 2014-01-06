>>> def chck(num):
	for x in range(num, 999999999, num):
		if all(x % n == 0 for n in range(1,20)):
			return x
	return None

>>> solution = chck(2520)

>>> if (solution is None):
	print "No number"
else:
	print "number found : ", solution