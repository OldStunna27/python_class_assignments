def showUs():
    print("This is a guess game.")
    ussdApp()

def ussdApp():

    databalance=0
    User=input(("Enter your code: "))
    if User==("*980#"):
        print("Welcome to your account")
    elif User !=("*980#"):
        print("Invalid code")
    else:
        print("Try again")
    account_features=('1.Data Plans', '2.Recharge', '3.Borrow Airtime', '4.Data Balance', '5.Mtn Share', '6.VAS', '7.NIN')
    buy_data_plans = ('Buy Data Plans', '1.Daily', '2.Weekly', '3.Monthly', '4.2-3Month', '5.Always ON', "6.Broadband", '7.family packs', '8.Hot Deals', '9.Free Youtube', '10.Manage Data', '0.Back')
    for each in account_features:
        print(each) 
    user_input=input("Please select your option: ")
    dataplans=("1.Daily", "2.Weekly", "3.Monthly")
    if dataplans == "1":
        print("1. 100MB/#20", "2. 1000GB/#300", "2. 5000GB/", "3. 10gb/#3000")
    print()
showUs()

    






#User=input(("Enter your code: "))
#account_features=['News', 'Account', 'settings', 'balance', 'deposit', 'cart', 'purchases']

#if User==("*980#"):
    #if User.lstrip().isdigit() and int(User):
        #print("Welcome")
#elif User !=("*980#"):
    #print("Invalid code")
#else:
    #print(account_features)








def guessGame():
    username = input("Enter your username: ")
    print(username + " welcome to guess game.")
    guessApp()


def guessApp():
    """This is a a guess game app"""

    points=0
    fruits=('mango', 'orange','pawpaw','cashew','water melon')
    #print(len(fruits))
    questions=('1.what is the total number of fruit in the basket','2. is apple one of the fruit in the basket', '3.guess any fruit you think is in the basket', '4.what number is pawpaw in the basket', '5. what number is water melon in the basket.')

    for each in questions:
        print(each)
        user_input=input('Enter your answer: ')
    if user_input ==  len(fruits):
        print(user_input)
        points+=20
        print(f"correct you just won {points} points")
    else:
        print("Lost")
        
    if user_input.strip().lower()=='no' or user_input.isalpha()=='no':
        points+=20
        print(f'correct! You just won ${points} points')
    else:
        print("Lost")

    if user_input.lstrip().isdigit() and int(user_input)==len(fruits):
        print(user_input)
        points+=20
        print(f'correct you just won ${points}')
    else:
        print("Lost")
        
        
    if user_input.lstrip().isalpha() in fruits:
        points+=20
        print(f'correct! You just won ${points}')

    if user_input.lstrip().isdigit() and int(user_input) == fruits.index('pawpaw')+1:
        points+=20
        print(f'correct! You won ${points}')
    else:
        print("Lost")

    if user_input.lstrip().isdigit() and int(user_input) == fruits.index('water melon')+1:
        points+=20
        print(f'correct! You have won ${points}')
    else:
        print("Lost")

    if points > 0:
        print(f'Congratulations! You won {points} points')
    else:
        print("Thank you for playing the guess game. Try again next time")
    print()
guessGame()