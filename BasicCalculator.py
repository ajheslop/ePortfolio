#Basic Calculator - Must include code comments 
#Must accept user input (include a prompt)

addNum1 = input("What is the first number?: ")
addNum2 = input ("What is the second number to add? ")
#Must store the input inside a variable
equals = int(addNum1) + int(addNum2)
#Must be able to accept whole numbers (21, 100,1000)
	#Data Type Integer
#Must be able to add two whole numbers together
	#2+2 operator
#Must be able to print out the sum of the two numbers that were input
#Must include a message along with the sum of the numbers e.g. “the sum of x plus x is: y”
print ("The sum of " + str(addNum1) + " plus " + str(addNum2) + " is: " + str(equals))
