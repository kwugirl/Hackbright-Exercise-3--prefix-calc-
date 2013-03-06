import arithmetic

def makeInt(myList):
	for i in range(1, len(myList)):
		myList[i] = int(myList[i])
	return myList

while True:
	user_input = raw_input("> ") #requests user to enter an expression
	tokens = user_input.split(" ") #separates the user's imput into a list 

	if tokens[0] == "q":
		break

	elif tokens[0] == "+":
		#print int(tokens[1]) + int(tokens[2])
		tokens = makeInt(tokens)
		print arithmetic.add(tokens[1], tokens[2])

	elif tokens[0] == "-":
		#tokens[1] = int(tokens[1]) # converted this into the makeInt function
		#tokens[2] = int(tokens[2])
		tokens = makeInt(tokens)
		print arithmetic.subtract(tokens[1], tokens[2])

	elif tokens[0] == "*":
		tokens = makeInt(tokens)
		print arithmetic.multiply(tokens[1], tokens[2])

	elif tokens[0] == "/":
		tokens = makeInt(tokens)
		print arithmetic.divide(tokens[1], tokens[2])

	elif tokens[0] == "square":
		tokens = makeInt(tokens)
		print arithmetic.square(tokens[1])

	elif tokens[0] == "cube":
		tokens = makeInt(tokens)
		print arithmetic.cube(tokens[1])

	elif tokens[0] == "pow":
		tokens = makeInt(tokens)
		print arithmetic.power(tokens[1], tokens[2])

	elif tokens[0] == "%":
		tokens = makeInt(tokens)
		print arithmetic.mod(tokens[1], tokens[2])

	else:
		print "I don't know what that means." 

