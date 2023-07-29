arr = "())(()"
print(arr.split())
lst = []
for i in arr:
	lst.append(i)
count = 0
if len(arr) >= 2 or len(arr) == 0:
	if lst[0] == ")":
		print(False)
	else:
		for i in lst:

			if i == "(":
				count+=1
			elif i == ")":
				count-=1
		if count == 0:
			print(True)
		else:
			print(False)
else:
	print(False)


