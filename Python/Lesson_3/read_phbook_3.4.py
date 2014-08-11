import string

def to_dict(items):
	book_dict = {}
	for i in range(0, len(items), 2):
		book_dict[int(items[i])] = items[i+1]
	return book_dict

def to_tuple_list(items):
	book_tuple_list = []
	for i in range(0, len(items), 2):
		contact = (int(items[i]), items[i+1])
		book_tuple_list.append(contact)
	return book_tuple_list

def to_sort_tuple_list(items):
	book_tuple_list_sorted = []
	for i in range(0, len(items), 2):
		contact = (int(items[i]), items[i+1])
		book_tuple_list_sorted.append(contact)
	book_tuple_list_sorted.sort()
	return book_tuple_list_sorted

def get_name(items):
	phone_number = input("Enter the phone number you need: ")
	for i in range(0, len(items)):
		if phone_number == items[i]:
			return items[i+1]


phonebook = open('phonebook.txt', 'r')
text = phonebook.read()
items = str.split(text)

to_sort_tuple_list(items)


