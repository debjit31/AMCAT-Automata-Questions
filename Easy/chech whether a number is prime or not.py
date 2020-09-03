## Check whether a given number is prime or not
def checkPrime(n):
	if n <=1:
		return False
	elif n == 2:
		return True
	else:
		for i in range(2, 1 + int(n**(1/2))):
			if n % i == 0:
				return False
		return True
n = int(input())
if checkPrime(n):
	print('Prime')
else:
	print('Not Prime')