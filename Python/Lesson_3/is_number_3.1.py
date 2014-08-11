def is_number(string):

	index = len(string) - 1
	dot_count = 0

	if string[0].isdigit() or string[0] == '-':
		while index > 0:
			if string[index].isdigit() or string[index] == '.':
				if string[index] == '.':
					dot_count += 1
			else:
				return False
			index -= 1
		if dot_count > 1:
			return False
		return True


	else:
		return False

user_string = input("Please enter your number: ")
print (is_number(user_string))