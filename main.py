print("Howdy world")




def multiplication():

    x = input("Give me a number to multiply:")
    y = input("What do you want it multiplied by?")

    z = int(x) * int(y)

    print("The result is " + str(z))

#multiplication()

def division():
    x = input("Give me a divident:")
    y = input("What do you want it divided by?")

    z = float(x) / int(y)

    print("The result is " + str(z))

#division()

def wide_boy_strings():
    user_str = input("Give me a string to  w i d e n \n")

    for char in user_str:
        print(char, end=" ")

#wide_boy_strings()

def wide_boy_strings2():
    user_str = input("Give me a string to  w i d e n \n")

    i = 0

    wide_str = ""

    for char in user_str:

        if i < len(user_str) - 1:
            wide_str = wide_str + char + " "
        else:
            wide_str = wide_str + char
        
        i += 1

    print(wide_str)
    

#wide_boy_strings2()

def for_loop_example():
    x = int(input("How many times should I run?"))

    for i in range(x):
        print("This loop is running for the "+ str(i+1) +" time.")

#for_loop_example()

def odd_or_even():
    x = int(input("Which number do you want me to check?"))

    if x % 2 == 0:
        print("The number " + str(x)+ " is even.")
    else:
        print("The number " + str(x)+" is am odd duck.")

#odd_or_even()

def ascii_sum():
    user_str = input("Give me a string for which you want the sum of the ASCII values of its chars: \n")

    str_size = len(user_str)

    i = 0

    sum = 0

    while(i < str_size):
        
        sum = sum + ord(user_str[i])
        i = i + 1

    print("The sum of all these ASCII values is ", sum )

#ascii_sum()

def string_flipper():
    user_str = input("Give me a string you want flipped or reversed \n")

    for char in reversed(user_str):
        print(char, end="")

#string_flipper()

user_input = int(input("Which function would you like to run?"))

if user_input == 0:
    multiplication()
elif user_input == 1:
    division()
elif user_input == 2:
    wide_boy_strings()
elif user_input == 3:
    for_loop_example()
else:
    print("Not a valid selection.")