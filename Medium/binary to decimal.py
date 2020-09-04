## Binary to decimal 
bin = input()
decn = 0
l = len(bin)-1
for i in range(len(bin)):
	decn += (int(bin[i]) * (2**l))
	l-=1
print(decn)
	
