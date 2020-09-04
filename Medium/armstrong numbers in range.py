## Armstrong Numbers in between intervals 

def armstrongNumbers(a, b):
	ans  = []
	for i in range(a, b+1):
		ns = str(i)
		p = len(ns)
		s=0
		for d in ns:
			s = s + int(d)**p
		if s == i:
			ans.append(i)
	return ans
a,b = list(map(int, input().split()))
print(armstrongNumbers(a,b))