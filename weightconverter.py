#User_weight=("what do you want to convert to(kg/lbs)? ")

#if User_weight=="kg":
    #lbs=float(input("what is your weight in pounds? "))
    #kg=lbs/2.20462
    #print(kg)
#if User_weight=="lbs":
    #kg=float(input("what is your weight in kilograms? "))
    #lbs= kg * 2.20462
    #print(lbs)

#thislist=["apple", "banana", "cherry", "cherry", "Cherry"]
#print(thislist)
#thislist.append ("pawpaw")
#print(len(thislist))
#list1=["apple", "banana", "orange", "cherry"]
#list2=[1, 2, 4, 6, 9]
#list3=[True, False, False]
#another_list=list(("orange", "potatoes", "onions"))
#print(another_list)
#print(list2)

#thisistuple=("Pelumi",)
#print(type(thisistuple))

#thistuple=tuple(("Orange", "Cake", "potatoes"))
#print(thistuple)
#print(type(thistuple))


#def covert_to_kg():
#pound =float(value. get()) * 2.20462.
#gram = float(value. get()) * 1000.
#ounce = float(value. get()) * 35.274.


#kg_weight=input("What is your weight in Kg? ")
#new_weight=kg_weight * 2.20462
#print(new_weight) + " lbs"

#User_weight=("what do you want to convert to(kg/lbs)? ")
#if User_weight=="kg":
    #lbs=float(input("what is your weight in pounds? "))
    #kg=lbs/2.20462
    #print(kg)
#if User_weight=="lbs":
    #kg=float(input("what is your weight in kilograms? "))
    #lbs= kg * 2.20462
    #print(lbs)

def weightconverter():
    print("This is a weight converter from kg to lbs.")
    weightapp()
    


def weightapp():
    """this is a weight converter"""
    weight = int(input('What is your weight? '))
    unit = input(('In (kg) or (lbs)? '))
    if unit.lower() == "kg":
        conversion = weight * 2.205
        print(f"Your weight in pounds is {conversion}lbs")
    else: 
        conversion = weight // 2.205
        print(f"Your weight in kilograms is {conversion}kg")
        print()
weightconverter()
