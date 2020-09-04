# In a town, houses are marked with English alphabets. 
# Committee in the town wants to renovate the houses. 
# They decided to renovate only houses named with vowels.
# Committee has given the list to members and asks them to identify the houses which are not renovated. 
# Write an algorithm to help the committee members to find houses which are not renovated.

house = input()
ans= ""
for i in range(len(house)):
	if house[i] != 'a' and house[i] != 'e' and house[i] != 'i' and house[i] != 'o' and house[i] != 'u':
		ans += house[i]
print(ans)
		