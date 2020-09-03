## fibonacci upto N value 

def fibouptoN(n):
	target = n
	a,b = 0,1
	while a+b < target:
		z = a+b
		print(z,end=' ')
		a = b
		b = z
		
n = int(input())
print(fibouptoN(n))