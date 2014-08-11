def power_of_two(x):
	""" Check if the figure is a power of two """
	while x > 2:
		x = x / 2

	return x == 2.0

user_number = int(input("Enter your number: "))
x = power_of_two(user_number)
print(x)