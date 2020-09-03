## Strong Number
def fact(n):
	f = [1,1]
	for i in range(2, n+1):
		f.append(f[-1] * i)
	return f
	
n = int(input())
ns = str(n)
factorials = fact(9)
s=0
for i in ns:
	s += factorials[int(i)]
print(s == n)