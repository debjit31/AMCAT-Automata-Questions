
## Primes in Range

import bisect as bi
def genPrimes(n):
	primes = [True for i in range(n+1)]
	p=2
	while p*p <= n:
		if primes[p] == True:
			for i in range(p*p, n+1, p):
				primes[i] = False
		p+=1
	ans=[]
	for i in range(2,n):
		if primes[i]:
			ans.append(i)
	return ans


low, high = list(map(int, input().split()))
primes = genPrimes(max(low,high))
li = bi.bisect(primes, low)
for i in range(li, len(primes)):
	print(primes[i], end= ' ')