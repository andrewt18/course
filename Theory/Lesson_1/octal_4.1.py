
def octal_normal(octal):
	"""octal to int converter"""

	integer = int(octal, 8)

	return integer

octal = input("Enter an hexadecimal number: ")  #Вводим число
x = octal_normal(octal)
print(x)