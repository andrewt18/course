def sieve(n):
	if n == 2:
		return n

	complete_list = list(range(2, n+1))		#Create a list until user's figure
	for x in complete_list:					#Every element will be tested
		index = 1							#Element's index in the list
		while index < len(complete_list):
			if complete_list[index] != x:
				if complete_list[index] % x == 0:
					complete_list.remove(complete_list[index])
			index += 1

	return complete_list
		


user_sting = int(input("Enter your number "))
print(sieve(user_sting))

