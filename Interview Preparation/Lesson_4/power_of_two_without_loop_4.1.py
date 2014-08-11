import math

def power_of_two(x):
	""" Check if the figure is a power of two """
	bin_x = bin(x)
	digit = int(bin_x[3:])
	print(digit == 0)
	

user_number = int(input("Enter your number: "))
x = power_of_two(user_number)
