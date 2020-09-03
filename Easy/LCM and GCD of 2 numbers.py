## GCD and LCM of 2 numbers
def _gcd(a,b):
	if a == 0:
		return b
	return _gcd(b%a, a)


a,b = list(map(int, input().split()))
g = _gcd(a,b)
print('GCD = ' , g)
print('LCM :- ', a*b//g)
