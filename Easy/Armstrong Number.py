## Armstrong Number
def checkArmstrong(n):
	num = str(n)
	n1 = len(num)
	s = 0
	for i in num:
		s += int(i) ** n1
	return s == n
n = int(input())
print(checkArmstrong(n))