import random
print('Try to guess the system number.')

count = 0
systemNumber = random.randint(1,100)

while systemNumber != "":
	mynumber = int(input("Enter a number: "))
	count += 1
	if (mynumber < 1) or (mynumber > 100):
		print('Please enter a number from 1 to 100: ')
		continue

	if mynumber < systemNumber:
		print('Your number is smaller than system number')
		continue

	if mynumber > systemNumber:
		print('Your number is bigger than system number')
		continue

	if mynumber == systemNumber:
		print('Correct! You have guessed with ' + str(count) + ' attempts!')
		break
input()
