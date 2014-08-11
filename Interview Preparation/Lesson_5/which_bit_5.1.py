def check_bit(digit, bit_count):
	return 1 & (digit >> bit_count)

digit = int(input('Enter a digit to check: '))
bit_count = int(input('Enter a bit to check: '))
print(check_bit(digit, bit_count))