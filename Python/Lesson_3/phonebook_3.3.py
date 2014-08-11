import random, string

def random_phonebook():

	numbers = set()
	while len(numbers) < 100000:
		rndm_number = random.randint(1000000, 9999999)
		numbers.add(rndm_number)

	names = set()
	while len(names) < 100000:
		name_length = random.randint(4, 10)
		name = ''.join(random.choice(string.ascii_lowercase) for i in range(name_length))
		up_name = name.capitalize()
		names.add(up_name)

	while len(numbers) > 0:
		phonebook.write(str(numbers.pop()) + "   " + names.pop() + "\n")
	
phonebook = open('phonebook.txt', 'x')
random_phonebook()