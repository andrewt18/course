def input_int(a, b):
	user_number = input("Please enter your number")
	while True:
		if user_number.isdigit():
			if (user_number >= a) and (user_number <= b):
				break
			else:
				print("Please enter a right number")
		else:
			print("Please enter a number")
	return user_number