import re
import unittest
import urllib.request


class Finder():
	def __init__(self, url, depth):
		self.url = url
		self.deep = depth
		self.mails = []
		# self.pattern = re.search(r'http://[\w-]+', self.url).group()
	cache = []

	def request(self, link):
		try:
			page = urllib.request.urlopen(link)
			data = str(page.read())
			return data
		except:
			return 'Nothing found'

	def email_checker(self, data):
		found = re.findall(r'[\w.-]+@[\w-]+\.[\w]+', data)
		return found

	def add_mails(self, data):
		maillist = self.email_checker(data)
		try:
			for i in maillist:
				if i not in self.mails:
					self.mails.append(i)
		except:
			pass

	def link_checker(self, data, new_links, db):
		found = self.link_finder(data)
		good_links = []
		try:
			for i in found:
				if '.img' in i or '.php' in i or '.pdf' in i:
					continue
				if i not in Finder.cache and i not in new_links and i not in good_links and i not in db:
					good_links.append(i)
		except:
			pass
		return good_links

	def link_finder(self, data):
		found = re.findall(self.url+'[\w/-]+', data)
		return found

	def create_output_file(self):
		output = open('output.txt', 'w')
		for i in self.mails:
			output.write(i+'\n')
		print('Thank you. Your output file is successful created.')

	def main(self):
		db = [self.url]
		new_links = []
		while self.deep > 0:
			for i in db:
				if self.deep == 1:#don't need to search new links
					print("Request to",i)#only to see what program does
					data = self.request(i)
					self.add_mails(data)
				else:
					print("Request to deep 2",i)
					data = self.request(i)
					self.add_mails(data)
					new_links.extend(self.link_checker(data, new_links, db))
			Finder.cache.extend(db)
			db = new_links
			new_links = []
			self.deep -= 1
		self.create_output_file()

url = input("Enter an URL in form: 'http://yoururl': ")
depth = int(input("How deep should the program search emails?: "))
check = Finder(url, depth)
check.main()



# class Unittests(unittest.Testcase):

# 	def finded_mails(self):
# 		given_site = ''
# 		given_email_list = [] #change to None if no email on site
# 		test = Finder()
# 		result = test.email_checker(request(given_site))
# 		checkEqual(given_email_list, result)

# 	def finded_links(self):
# 		given_site = ''
# 		given_link_list = []
# 		test = Finder()
# 		result = test.link_checker(request(given_site))
# 		checkEqual(given_link_list, result)

# 	def checkEqual(element1, element2):
# 		return len(element1) == len(element2) and sorted(element1) == sorted(element2)