def intersect(rect_one, rect_two):
	x = None
	if (rect_two[0][0] - rect_one[0][1] >= 0) or (rect_one[0][0] - rect_two[0][1] >= 0):
		x = False
	if (rect_two[1][1] - rect_one[1][0] >= 0) or (rect_one[1][1] - rect_two[1][0] >= 0):
		x = False
	else:
		x = True
	return x

rect_one = ((0,5), (5,0))
rect_two = ((3,8), (7,3))

x = intersect(rect_one, rect_two)
print(x)