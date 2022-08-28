# -------------------------------- GET THE SUM OF TWO NUMBERS BY USING A FUNCTION --------------------------------------#
# Creating function that adds the two numbers together.
def solveMeFirst(a, b):
    return a + b


# Takes in first number from user input:
num1 = int(input("Type in the first number: "))
# Takes in second number from user input:
num2 = int(input("Type in the second number: "))
# Replaces the two numbers with the a and b variables in the function and tying them to it's own variable.
result = solveMeFirst(num1, num2)

# Printing the result.
print(result)


# -------------------------------------- FIND THE SUM OF AN ARRAY OF INTEGERS ------------------------------------------#
# Creating function that utilizes Pythons built in "sum" function to sum up the integers in the array.
def simpleArraySum(ar):
    return sum(ar)


# Our array of integers
ar = [1, 2, 3]

sum = simpleArraySum(ar)

print(sum)

# The problem over can also be solved with a for loop, like this:

ar = [1, 2, 3]
total = 0

for number in ar:
    total += number
# Note that you have to put the print outside of the loop so that it doesn't print out total during the loop.
# In that case it would first add 1 + 2 and return that as total, and then return 6.
print(total)


# Solving this through recursion:

def sum_numbers(numbers):
    if len(numbers) == 0:
        return 0
    return numbers[0] + sum_numbers(numbers[1:])


ar = [1, 2, 3]
total = sum_numbers(ar)
print(total)
