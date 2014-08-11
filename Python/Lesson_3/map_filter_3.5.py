def my_map(func, items):
	new_list = []
	for i in range(len(items)):
		new_list.append(func(items[i]))
	return new_list

def my_filter(func, items):
	new_list = []
	for i in range(len(items)):
		if func(items[i]) == 0:
			new_list.append(items[i])
	return new_list

def func(x):
	return x % 2


items = [1, 2, 3, 4, 5]
print(my_map(func, items))
print(my_filter(func, items))