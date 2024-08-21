def showUs():
    print("This is a multiplication table.")
    multiplicationApp()


def multiplicationApp():
    """This is a function for a mulitiplication table from 1-5"""

    multiplication_table=("Welcome to multiplication table")
    print(multiplication_table)
    userinput=input("Choose table from 1-5: ")
    table1=["1 x"]
    text1=["1 = 1", "2 = 2", "3 = 3", "4 = 4", "5 = 5", "6 = 6", "7 = 7", "8 = 8", "9 = 9", "10 = 10", "11 = 11", "12 = 12"]
    table2=["2 x"]
    text2=["1 = 2", "2 = 4", "3 = 6", "4 = 8", "5 = 10", "6 = 12", "7 = 14", "8 = 16", "9 = 18", "10 = 20", "11 = 22", "12 = 24"]
    table3=["3 x"]
    text3=["1 = 3", "2 = 6", "3 = 9", "4 = 12", "5 = 15", "6 = 18", "7 = 21", "8 = 24", "9 = 27", "10 = 30", "11 = 33", "11 = 36"]
    table4=["4 x"]
    text4=["1 = 4", "2 = 8", "3 = 12", "4 = 16", "5 = 20", "6 = 24", "7 = 28", "8 = 32", "9 = 36", "10 = 40", "11 = 44", "12 = 48"]
    table5=["5 x"]
    text5=["1 = 5", "2 = 10", "3 = 15", "4 = 20", "5 = 25", "6 = 30", "7 = 35", "8 = 40", "9 = 45", "10 = 50", "11 = 55", "12 = 60"]

    if userinput ==("1"):
        print("Table 1")
        for table in table1:
            for text in text1:
                print(f"{table} {text}")
    elif userinput==("2"):
        print("Table 2")
        for table in table2:
            for text in text2:
                print(f"{table} {text}")
    elif userinput==("3"):
        print("Table 3")
        for table in table3:
            for text in text3:
                print(f"{table} {text}")
    elif userinput==("4"):
        print("Table 4")
        for table in table4:
            for text in text4:
                print(f"{table} {text}")
    elif userinput==("5"):
        print("Table 5")
        for table in table5:
            for text in text5:
                print(f"{table} {text}")
    else:
        print("Enter a valid table number")
    print()
showUs()
