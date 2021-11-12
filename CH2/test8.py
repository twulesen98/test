#Generate a hailstone sequence

number_str = input("Emter a positive interger: ")
number = int(number_str)
count = 0

print("Starting with number: ", number)
print("Sequence is: ", end = '')

while number > 1:  #stop when the sequence reaches 1

	if number % 2:  # number is odd
		number = number*3 + 1
	else:		# number is even
		number = number / 2
	print(number, ",", end = '')  # add number to sequence
	
	count += 1
	
else:
	print()  # blank line for nice output
	print("Sequence is ", count, "number long")
	
