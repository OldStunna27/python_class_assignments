def showUs():
    print("This is a number checker for odd and even number")
    numberCheckerApp()

def numberCheckerApp():
    """This is a function to check for odd and even number"""

    num_input = input("Enter a number: ")
    if num_input == " ":
        print("Input can't be empty")
    elif num_input.lstrip("-").isdigit():
        num = int(num_input)
        #print(type(num))
        result = num % 2
    if result == 0:
        print("The number you supplied is an even number")
    elif result !=0:
        print("The number you supplied is an odd number")
    else:
        print("invalid entry. Please enter a valid integer.")
    print()
showUs()

