
def hexadecimal_normal(hexadecimal):
	"""hexadecimal to base 7 converter"""

	integer = int(hexadecimal, 16)
	base_seven = (integer // 7 * 10) + (integer % 7)


	return base_seven

hexadecimal = input("Enter an hexadecimal number: ")  #Вводим число
x = hexadecimal_normal(hexadecimal)
print(x)