# Shopping bill calculator
# Write a python program that will keep adding a stream of numbers inputted by the user. 
# The adding stops as soon as the user presses "q" key on the keybord.

sum = 0
while(True):
    userInput = input("Enter the item price or press q to quit: \n")
    if (userInput!='q'):
        sum = sum + int(userInput)
        print(f"Order total so far: {sum}")

    else:
        print(f"Your bill total is {sum}. Thanks for shopping with us.")
        break