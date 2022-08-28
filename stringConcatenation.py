# --------------------------------------------- STRING CONCATENATION ---------------------------------------------------#

# String concatenation is how to tie string elements together with variables and it can be done in a few different ways

# print("Subscribe to " + youtuber)
# print("Subscribe to {}" .format(youtuber))
# print(f"subscribe to {youtuber}") This is also called an f string and is what I'll be using the most.

# An example of an f string would be this:

# STAGE 2 (create variables for each of the variables in the f-string):

adj = input("Type in an adjective: ")
verb1 = input("Type in a verb: ")
verb2 = input("Type in a verb: ")
famousPerson = input("Type in the name of a famous person: ")

# STAGE 1 (create a variable holding string concatenation):
myText = f"Computer programming is so {adj}! It makes me so excited all the time because I love to {verb1}. Stay " \
         f"hydrated and {verb2} like you are {famousPerson}."

# STAGE 3 (Create a print statement):
print(myText)