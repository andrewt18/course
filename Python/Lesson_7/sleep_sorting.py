from time import sleep
from threading import Thread

def sleep_sort(arg):
	sleep(arg)
	sorted_items.append(arg)
def sort(lst):
	threads = []
	for i in lst:
		t = Thread(target=sleep_sort, args=(i,))
		t.start()
		threads.append(t)
	for a in threads:
		t.join()

sorted_items = []
lst = [1, 4, 3, 9, 11, 2]
sort(lst)
print(sorted_items)