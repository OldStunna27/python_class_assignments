def guessGame():
    print("Welcome to guess game")
    print()
    guessApp()

def guessApp():
    """This is a a guess game app"""
    username = input("Enter your username: ")
    print(f"{username} This is a guess game that allow you to play with fruits in the basket.")
    print()

    cash_prize=0
    fruits=('mango', 'orange','pawpaw','cashew','water melon',"apple", "pineapple")
    #print(len(fruits))
    questions=('1.What is the total number of fruit in the basket?','2.Is carrot one of the fruit in the basket?', '3.Guess any fruit you think is in the basket?', '4.What number is cashew in the basket?', '5.What number is water melon in the basket?.', "6.What number is mango in the basket?", "7.What number is orange in the basket?", "8.What number is pawpaw in the basket?", "9.Is apple one of the fruit in the basket?", "10.Guess the last fruit in the basket")

    for each in questions:
        print(each)
        user_input=input('Enter your answer: ')
        
        
        if each.startswith('1'):

            if user_input.lstrip().isdigit() and int(user_input)==len(fruits):
                cash_prize+=500
                print(f'Correct you just won ${cash_prize}')
            else:
                print('Incorrect. You have lost $500')
    
        elif each.startswith('2'):
            if user_input.strip().lower()=='no' or user_input.isalpha()=='No' or user_input.capitalize()== "NO":
                cash_prize+=500
                print(f'Correct! You just won ${cash_prize}')
            else:
                print('Incorrect. You lost $500')

        elif each.startswith('3'):
            if user_input in fruits:
                cash_prize+=500
                print(f'correct! You just won ${cash_prize}')
            else:
                print('Incorrect. You lost $500')

        elif each.startswith ('4'):
            if user_input.lstrip().isdigit() and int(user_input) == fruits.index('cashew')+1:
                cash_prize+=500
                print(f'Correct! You just won ${cash_prize}')
            else:
                print('Incorrect.You lost $500')

        elif each.startswith('5'):
            if user_input.lstrip().isdigit() and int(user_input) == fruits.index('water melon')+1:
                cash_prize+=500
                print(f'Correct! You just won ${cash_prize}')
            else:
                print(f'Incorrect. You lost $500')
        
        elif each.startswith("6"):
            if user_input.lstrip().isdigit() and int(user_input) == fruits.index("mango")+1:
                cash_prize+=500
                print(f'Correct! You just won ${cash_prize}')
            else:
                print(f'Incorrect. You $500')
        
        elif each.startswith("7"):
            if user_input.lstrip().isdigit() and int(user_input)==fruits.index("orange")+1:
                cash_prize+=500
                print(f'Correct! You just won ${cash_prize}')
            else:
                print(f'Incorrect. You lost $500')
        
        elif each.startswith("8"):
            if user_input.lstrip().isdigit() and int(user_input)==fruits.index("pawpaw")+1:
                cash_prize+=500
                print(f"Correct! You just won ${cash_prize}")
            else:
                print(f"Incorrect. You lost $500")
        
        elif each.startswith("9"):
            if user_input.isalpha() and str(user_input)== "yes" or str(user_input).upper()=="YES" or str(user_input)=="Yes":
                print(f"Correct! You won ${cash_prize}")
            else:
                print(f"Incorrect! You lost $500")
        
        elif each.startswith("10"):
            if user_input.isalpha() and str(user_input)=="pineapple":
                cash_prize+=500
                print(f"Correct! You just won ${cash_prize}")
            else:
                print(f"Incorrect! You lost $500")

        else:
                print('error')
                print()
        if cash_prize > 0:
            print(f" {username} congratulations! Your total prize is ${cash_prize}.")
        else:
            print(f"{username} thank you for playing the guess game. Try again next time")
        print()
guessGame()























