import re
import unittest
import urllib.request

class Finder:
	def __init__(self): #, url, depth):
		self.url = ''
		self.depth = 0
		self.db = []

	def request(self, url):
		try:
			page = urllib.request.urlopen(url)
			data = str(page.read())
			return data
		except:
			return 'Nothing found'	

	def create_txt(self, mail_list):
		mails = open("mails.txt", "w")
		for i in mail_list:
			mails.write(i + "\n")
		print('Thank you. Your output file is successful created.')

	def main(self):
		self.url = input("Enter an URL in form: 'http://yoururl': ")
		self.depth = int(input("How deep should the program search emails?: "))
		self.db.append(self.url)
		mails = Mails()
		links = Links()
		iter_index = 0
		while self.depth > 0:
			links_to_add = []
			for i in range(iter_index, len(self.db)):
				print("try to request:", self.db[i])
				data = self.request(self.db[i])
				mails.add_mails(data)
				if self.depth > 1:
					links_to_add.extend(links.update_links(data, self.db, links_to_add, self.url))
			iter_index = len(self.db)
			self.db.extend(links_to_add)
			self.depth -= 1

		self.create_txt(mails.mail_list)

class Mails:
	def __init__(self):
		self.mail_list = []
	def find_mails(self, data):
		founded_mails = re.findall(r'[\w.-]+@[\w-]+\.[\w]+', data)
		return founded_mails
	def add_mails(self, data):
		founded_mails = self.find_mails(data)
		try:
			for i in founded_mails:
				if i not in self.mail_list:
					self.mail_list.append(i)
		except:#if nothing found
			pass

class Links:
	def __init__(self):
		self.links_list = []
	def find_links(self, data, url):
		founded_links = re.findall(url+'[\w/-]+', data)
		return founded_links
	def check_links(self, founded_links, db, links_to_add):
		for link in founded_links:
			if '.pdf' in link or '.png' in link or '.jpg' in link or 'cache' in link or 'uploads' in link:
					continue
			if link not in self.links_list and link not in db and link not in links_to_add:
				self.links_list.append(link)
	def add_links(self, data, db, links_to_add, url):
		founded_links = self.find_links(data, url)
		filtred_links = self.check_links(founded_links, db, links_to_add)
	def update_links(self, data, db, links_to_add, url):
		self.links_list.clear()
		self.add_links(data, db, links_to_add, url)
		return self.links_list


check = Finder()
check.main()

class TestFoundedItems(unittest.TestCase):

	tested_link = 'http://heller.ru/blog/'
	tested_mails = ['heller@heller.ru', 'heller@riseup.net']
	tested_links_count = 162
	def test_founded_mails(self):
		#Проверка найденных емайлов на определённой странице
		data = Finder().request(TestFoundedItems.tested_link)
		test = Mails().find_mails(data)
		self.assertEqual(TestFoundedItems.tested_mails.sort(), test.sort(), "Email-test failed")


	def test_founded_links(self):
		#Проверка найденных ссылок на определённой странице
		data = Finder().request(TestFoundedItems.tested_link)
		test = Links().find_links(data, TestFoundedItems.tested_link)
		self.assertEqual(len(test), TestFoundedItems.tested_links_count, "Link-test failed")

if __name__ == '__main__':
	unittest.main()