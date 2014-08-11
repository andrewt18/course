def check_strings_without_11(string_length):
	strings_count = 0
	for i in range((2**string_length) - 1):
		if '11' not in bin(i):
			strings_count += 1
	return strings_count


string_length = int(input('How long should be a string: '))
print(check_strings_without_11(string_length))