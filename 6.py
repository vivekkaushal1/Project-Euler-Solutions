>>> total, sqsum, ans = 0, 0, 0
>>> total = sum(int(el**2) for el in range(1, 101))
>>> sqsum = sum(int(a) for a in range(1, 101))**2
>>> ans = sqsum - total
>>> print ans
