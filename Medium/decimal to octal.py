## decimal to octal 
n = int(input())
oct = ""
while n > 0:
	r = n%8
	oct = str(r) + oct
	n = n//8
print(oct)
	