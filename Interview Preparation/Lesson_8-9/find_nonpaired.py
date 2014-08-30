def single(lst):
	single1 = 0
	single2 = 0
	for i in lst:
		count = 0
		for a in lst:
			if i == a:
				count += 1
		if count == 1:
			single1 = single2
			single2 = i
	return single1, single2

lst = [2, 56, 23, 5, 7, 5, 7, 2]
print(single(lst))