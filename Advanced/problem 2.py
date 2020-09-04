# Program to find the frequency of characters in a string is discussed here. 
# Given a string, the occurrence or frequency of all the characters in the string are 
# counted and displayed as output.

s = input()
freq = [0 for _ in range(26)]
for i in s:
	if i == ' ':
		continue
	else:
		freq[ord(i)-ord('a')] += 1
letters = set(s)
for i in letters:
	if i == ' ':
		continue
	else:
		print(i + '->' + str(freq[ord(i)-ord('a')]), end=' ,')
	
		