## Abundant Number 
def getDivisors(n):
	if n == 1:
		return 1
	else:
		d,s=[],0
		for i in range(1, 1+int(n**(1/2))):
			if n % i == 0:
				if i == n//i:
					s += i
				else:
					s = s + i + (n//i)
		s=s-n
		return s
n = int(input())
su = getDivisors(n)
if su > n:
	print('Abundant Number')
else:
	print('Not Abundant Number')