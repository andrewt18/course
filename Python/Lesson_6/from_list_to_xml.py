import re

def how_type(string):
	try:
		re.search(r'\w+:', string).group()
		return "tag"
	except:
		return "main"

def define_main(line):
	line = line.strip()
	line = line.replace(" ", "_")
	return line #"</" + line + ">" 

def add_main(line, string):
	line = line.strip()
	line = line.replace(" ", "_")
	return string + "<" + line + ">" + "</" + line + ">" 

def add_note(string, main_tag):
	to_add = "<note></note>" 
	add_index = string.rfind("</" + main_tag)
	return string[:add_index] + to_add + string[add_index:]

def add_tag(line, string):
	colon_index = line.index(":")
	tag_to_add = line[:colon_index]
	tag_value = line[colon_index + 1:]
	to_add = "<" + tag_to_add + ">" + tag_value + "</" + tag_to_add + ">" 
	add_index = string.rfind("</note")
	return string[:add_index] + to_add + string[add_index:]

def create_xml(string):
	data = open("output.xml", "w")
	data.write(string)
	data.close()

def file_len(fname):
    with open(fname) as f:
        for i, l in enumerate(f):
            pass
    return i + 1

def get_formatted(text):
	line_count = file_len(text)
	data = open(text, 'r', encoding='utf-8')
	string = '<?xml version="1.0" encoding="UTF-8"?>'
	main_tag = ""
	first_tag = ""
	need_first_tag = False
	for i in range(line_count):
		line = data.readline()
		if line == "\n" or line == "":
			continue
		else:
			tp = how_type(line)
			if tp == "main":
				main_tag = define_main(line)
				string = add_main(line, string)
				need_first_tag = True
			elif need_first_tag:
				first_tag = line[:line.index(":")]
				string = add_note(string, main_tag)
				string = add_tag(line, string)
				need_first_tag = False
			elif line[:line.index(":")] == first_tag:
				string = add_note(string, main_tag)
				string = add_tag(line, string)
			else: 
				string = add_tag(line, string)
	create_xml(string)
	print("Your xml file 'output.xml' is successfully created")



to_format = input("Enter your file to fromat to XML: ")
get_formatted(to_format)