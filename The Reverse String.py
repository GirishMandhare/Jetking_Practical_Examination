Python 3.10.11 (tags/v3.10.11:7d4cc5a, Apr  5 2023, 00:38:17) [MSC v.1929 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
>>> def reverse_vowels(str1):
... 	vowels = ""
... 	for char in str1:
... 		if char in "aeiouAEIOU":
... 			vowels += char
... 	result_string = ""
... 	for char in str1:
... 		if char in "aeiouAEIOU":
... 			result_string += vowels[-1]
... 			vowels = vowels[:-1]
... 		else:
... 			result_string += char
... 	return result_string
... print(reverse_vowels("w3resource"))
... print(reverse_vowels("Python"))
... print(reverse_vowels("Perl"))
... print(reverse_vowels("USA"))
