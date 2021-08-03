## Creating Acronyms using Python

# Taking a string user input
user_input = str(input("Enter a phrase: "))

# Lets split the sentence
text = user_input.split()

# Variable for storing the acronym of a phrase
a = " "

# Lets run a loop and taking the first letter of the words and converting to uppercase
for i in text:
    a = a + str(i[0]).upper()
print(a)