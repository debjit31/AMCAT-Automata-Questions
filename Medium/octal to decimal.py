## 0ctal to decimal 
oct = input()
p = len(oct)-1
s=0
for i in oct:
	s = s + int(i)*(8**p)
	p-=1
print(s)
