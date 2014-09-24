def permutations(lst):
	if len(lst) == 1 or len(lst)==0:
		return lst
	res = []
	change_index = 1
	var = len(lst) - 1
	while True:
		if lst not in res:
			res.append(lst[:])
			if var == 2:
				var = len(lst) - 1
			else:
				var -= 1
			lst[var], lst[var-1] = lst[var-1], lst[var]
		else:
			if change_index == len(lst):
				break
			lst[0], lst[change_index] = lst[change_index], lst[0]
			change_index += 1

	return res
print(permutations([1,2]))
