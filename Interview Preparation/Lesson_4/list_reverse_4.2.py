def list_reverse(x):
	""" Reverse a list """
	x = x[::-1]

	return x
	

mylist = [1, 2, 3, 4, 5]
mylist = list_reverse(mylist)
print(mylist)

