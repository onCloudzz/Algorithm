aList =[chr(i) for i in range(65,91)] + [chr(i) for i in range(97,123)]
M = input()
for i in range(len(M)):
	print(aList[(aList.index(M[i])+26)%52],end="")