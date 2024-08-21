def showUs():
    print()
    pallindromeChecker()


def pallindromeChecker():
    """This is a Pallindrone checker and check for words"""
    user_input=input("please enter a word: ")
    if user_input == "":
        print("can't be empty")
    elif user_input == user_input[::-1]:
        print("This is a palindrome")
    else:
        print("Not a palindrone")
    print()
showUs()
