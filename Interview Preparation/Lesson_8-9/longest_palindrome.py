def longest_palindrome(string):
	palindroms = []
	if string == string[::-1]:
		palindroms.append(string)
	else:
		palindroms.append(longest_palindrome(string[1:]))
		palindroms.append(longest_palindrome(string[:-1]))
	
	return max(palindroms, key=len)

x = "xxabcbaay"
print(longest_palindrome(x))