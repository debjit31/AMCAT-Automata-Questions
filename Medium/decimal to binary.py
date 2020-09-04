## decimal to binary 
n = int(input())
b = ""
while n > 0:
	r = n%2
	b = str(r) + b
	n = n//2
print(b)