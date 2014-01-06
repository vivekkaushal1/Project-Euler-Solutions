>>> a, b, n, sum = 0, 1, 0, 0
>>> result = []
>>> num = []
>>> while (b < 400000):
	result.append(a)
	a, b = b, a+b

>>> for n in result:
	if n % 2 == 0:
		num.append(n)

>>> for x in num:
	sum += x

>>> print sum