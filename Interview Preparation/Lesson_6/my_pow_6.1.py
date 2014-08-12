
#Идея решения взята отсюда
#https://de.wikipedia.org/wiki/Bin%C3%A4re_Exponentiation#Pseudocode_2
def my_pow(x, n):
	if n < 0:
		raise ValueError("Your exponen must be non-negative")
	res = 1
	iteration = x
	while n > 0:
		if n % 2 == 1:
			res = res * iteration
		iteration = iteration * iteration
		n = n//2
	return res




print(my_pow(2, 0))
print(my_pow(3, 3))
print(my_pow(4, 4))