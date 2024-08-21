def setExam():
    print("Questions for cbt on set method.")
    print()
    setApp()

def setApp():
    commercial_class = {"Agriculture", "Economics", "Mathematics", "English Language", "Geography", "Financial Accouunting", "Commerce", "Further Mathematics", "Biology", "Yoruba Language", "Agricultural Science", "Government", "Religion and Moral Instructions", "Civic Education", "Government"}
    science_class = {"Chemistry", "Physics", "Biology", "Mathematics", "English Language", "Geography", "Further Mathematics","Data Processing", "Animal Husbandry", "Agricultural Science", "Religion and Moral Instructions", "Yoruba Language", "Civic Education", "Animal Husbandry", ""}
    art_class = {"History", "Literature in English", "Yoruba Language", "Government", "Religion and Moral Instructions", "Civil Education", "Economics", "Mathematics", "English Language", "French", "Data Processing", "Further Mathematics", "Biology", "Christian Religious Knowledge", "Animal Husbandry"}
    #new_class = set(("Data Science", "Data Structure", "Programming Language"))
    #new_class1 = tuple((new_class))
    for each in art_class, science_class, art_class:
        print(each)
    #print(len(art_class))
    #print(type(commercial_class))
    #diff_result=art_class.difference()
    #print(diff_result)

    #print(type(art_class))
    #print(len(science_class))
    #print(type(new_class1))
    #print(new_class1)

    #for each in commercial_class:
        #print(each)
    #for each in art_class:
        #print(each)

    #commercial_class.issubset(art_class)
    #print(commercial_class)
    #userinput = input(("Please enter your Department: "))
    #if userinput == "":
        #print("Department can't be empty")
    #if userinput == str("Commercial"):
        #print(f"your subjects are {commercial_class}")

    #if userinput == str("Science"):
        #print(f"your subjects are {science_class}")

    #if userinput == str("Art"):
        #print((f"your subjects are {art_class}"))

    question = {"1.How many class offerring Mathematics?", "2.How many class offering Chemistry?", "3. What is the subjects offered in art and science class?", "3.What is the subjects offered in Commercial Class and Art class", "4.What is the subject offered in the Science and Commercial Class?", "5. What is the total subjects offered in all the 3 classes?", "6.What course is not offered in both science and art class?", "7.What is the membership subject for every class(course offered in the 3 classes?"}

    for each in question:
        print(each)
    user_input1=input('enter your answer>>')

    if each.startswith('1'):

        if user_input1.lstrip().isdigit() and int(user_input1)== commercial_class.intersection(art_class):
            print(user_input1)

            print(f'Correct')
        else:
            print('Incorrect. You have lost $500')
    elif each.startswith("2"):
        if user_input1 == science_class.difference(art_class):
            print("Correct")
        else:
            print("enter answer")
        print()
setExam()





