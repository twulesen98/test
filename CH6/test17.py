def are_anagrams (wordl, word2):
	"""Return True, if words are anagrams."""
	#2 Sort the characters of the words 
	wordl_sorted = sorted (word1)		#sorted returns a sorted list
	word2_sorted = sorted (word2)

	#3. Check that the sorted words are identical. 
	return wordl_sorted == word2_sorted

print ("Anagram Test")

#1. Input two words.
two_words = input ("Enter two seperated words: ")
word1,word2 = two_words.split() 	# split into a list of words

if are_anagrams(word1,word2):      	# return true or false
	print ("The words are anagrams.")
else:
	print("The words are not anagrams.")
