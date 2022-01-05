data_file= open("dic.txt", "r")
def clean_word(word):
	"""Return word in lower case stripped of whitespace."""
	return word.strip().lower()
# main program
for word in data_file:      
	word= clean_word(word) 
	if len(word) <= 6:      
		continue
print(word)
