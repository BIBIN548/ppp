print("hello world")

def modulo_calculator(): # for defining modulo calculator
    x = float(input(" please enter the numerator: "))
    y = float(input("please enter the denominator: "))

    remainder = x % y

    print(" the remainder of " + str(x) + " and " + str(y) + " is " + str(remainder))

#modulo_calculator()
# for defining modulo calculator
# next the function takes the input from the use and store it in x
#  next it takes the input from user and store it in y
# in reminder it do the calculations % modulo function and print the result.



def Integer_division():
    x = int(input(" please enter the numerator: "))
    y = int(input("please enter the denominator: "))

    z = x / y

    print(" the sum of " + str(x) + " and " + str(y) + " is " + str(z))

#Integer_division()
# def function defines the function integer div
# takes input from user and store it in x and y 
# in the next line does the calculation / division and print the result.

def for_loop():
    x = int(input("How many times should I run?"))

    for i in range(x):
        print("This loop is running for the "+ str(i+1) +" time.")

#for_loop()
# def defines the function foor loop
# it takes input from user and store it in the variable x
# next for loop that iterates x number of times.
# i is the loop variable takes each value
# next the loop run for str i + 1
# and prints the value

def float_integer_calculation():
    x = (input("give me the first number:"))
    y = (input("give me the second number:"))

    div = float(x) / int(y)
    add = float(x) + int(y)
    diff = float(x) - int(y)
    product = float(x) * int(y)
    modulus = float(x) % int(y)

    print("The result of", x, "divided by", y, "is", div)
    print("The result of", x, "added by", y, "is", add)
    print("The result of", x, "subtracted by", y, "is", diff)
    print("The result of", x, "mutiplied by", y, "is", product)
    print("The result of", x, "modulus", y, "is", modulus)

#float_integer_calculation()
# def defines the float integer function
# next it ask the user to enter two integer and store it in the variable x and y
# next it converts x to a float and y to an integer.
# it performs div, add, sub, mult and modulus
# then it prints the corresponding results

def print_ascii_string_value():
    user_str = input("Give me a string for which you want the sum of the ASCII value of its characters:\n")
   
    str_size = len(user_str)
    i = 0
    sum = 0

    while (i < str_size):
        sum = sum + ord(user_str[i])
        i = i + 1

    print("The sum of all this ASCII value is ", sum)

#print_ascii_string_value()
# def ascii value . this ask the user to enter a character and print the ascii value.
# calculates the length of user str and stores it in the variable str size.
#i is incremented by 1
# then it prints the result

def change_machine():
    amount = float(input("Please enter the amount:"))
    dollars = int(amount)
    cents = int(round((amount - dollars) * 100))
    quarters = cents // 25
    cents %= 25
    dimes = cents // 10
    cents %= 10
    nickels = cents // 5
    cents %= 5

    print("The return for", amount, "is", quarters, "quarters,", dimes, "dimes,", nickels, "nickels,", "and", cents, "cents.")

#change_machine()
# def defines the function change machine
# it asks the user for float input
# after that it calculates the number of quarters by performing integer division with 25 cents. The result is stored in the variable quarters.
# then it check it with cent by modulo operation
# next calculate the number of dime 
#calculate the number of nickels.
#next it prints the number of quarters, dimes, nickels, and remaining cents for the given amount.

import random

def rock_paper_scissors():
    number_choice = 0
    while number_choice < 1 or number_choice > 3:
        number_choice = int(input("Select:\n 1.Rock\n 2.Paper\n 3.Scissors\n"))

    ai_number_choice = random.randint(1, 3)

    if number_choice == ai_number_choice:
        result = "Draw"
    elif number_choice == 1:
        result = "Victory" if ai_number_choice == 3 else "Loss"
    elif number_choice == 2:
        result = "Victory" if ai_number_choice == 1 else "Loss"
    elif number_choice == 3:
        result = "Victory" if ai_number_choice == 2 else "Loss"

    choices = {1: "Rock", 2: "Paper", 3: "Scissors"}
    print("You chose " + choices[number_choice] + ", AI chose " + choices[ai_number_choice] + ". Result: " + result)

#rock_paper_scissors()
#def defines the function rock paper scissor
#then number choice variable is 0
#after that the while loop is executed and the number choice is between 1 and 3
#then it asks the user to input their choice
#the AI choice is assigned to the value to AI number choice
#next it compares number nchoice and ai number choice to determine the result of the game Victory, Loss, or Draw and assigns this value to the variable result
#it prints the user choice, AI choice and the game result

def mario_wins():
    climbnum = int(input("How many stairs should Mario climb to finish the level?"))

    while climbnum < 1 or climbnum > 10:
        climbnum = int(input("How many stairs should Mario climb to finish the level?"))

    for i in range(climbnum):
        for j in range(climbnum - i):
            print(" ", end="")
        for j in range(i + 2):
            print("#", end="")
        print("   ", end="")
        if i == 0:
            print("|>", end="")
        elif i == climbnum - 1:
            print("#", end="")
        else:
            print("|", end="")
        print()

#mario_wins()
#def defines mario wins function
#next the while loop gets executed
#then the climnum is between 1 and 10
#if the user enter more than 10 or less than 1 the function asks the user to input another value
#for loop is executed
#in the for loop the pattern is created by incrementing the i value
#after that it prints the result






user_input = int(input("Which function would you like to run?"))

if user_input == 0:
    modulo_calculator()
elif user_input == 1:
    Integer_division()
elif user_input == 2:
    for_loop()
elif user_input == 3:
    float_integer_calculation()
elif user_input == 4:
    print_ascii_string_value()
elif user_input == 5:
    change_machine()
elif user_input == 6:
    rock_paper_scissors()
elif user_input == 7:
    mario_wins()
else:
    print("Not a valid selection.")

    #this code allows the user to choose which function to run based on their input.
    #if and elif functioin is used to call corrsponding function
    #if user enter invalid number the else function is executed and it asks the user to enter a valid number.






   




