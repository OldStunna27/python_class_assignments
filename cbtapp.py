def showUs():
    print("This is a cbt exam app.")
    cbtApp()

def cbtApp():

    mark = 0
    #matric_number = input("Matric number: ")
    student_name = input("Student name: ").lstrip().lower()
    department = input("Department: ").isalpha()
    level = input("Enter your level: ").isalpha() 
    date = input("Enter date: ")

    matric_number =["2022001386", "2022003676"]
    password = ["Pelumi1"]

    matric_number = input("Enter your Matric Number: ")
    password1 = input("Enter your password: ")


    if password1 in password:
        print(f"{student_name} Welcome to your CBT Test")
        test = {"1. What is the name of Nigeria President? (a)Olusegun Obasanjo (b)Sanni Abacha (c)Asiwaju Bola Tinubu": "c",
            "2. How many classes of food do we have? (a)3 (b)6 (c)13": "b",
            "3. What is the Capital city of South Africa? (a)Cape Town (b)Johannesburg (c)Abuja": "b",
            "4. Water occupied 70 percent of the earth surface? (a)Yes (b)No": "a",
            "5. What country is the last World Cup winner? (a)Argentina (b)Brazil (c)Nigeria": "a",
            "6. Who is the 1st runner up in the 2024 Afcon competition? (a)Ghana (b)Nigeria (c)France": "b",
            "7. Who is the ex president of United State of America? (a)Putin (b)Joe Biden (c)Donald Trump": "c",
            "8. How many states is in Nigeria? (a)60 (b)36 (c)35": "b",
            "9. What is the name of Oyo state governor (a)Eng. Seyi Makinde (b)Sen. Ademola Adeleke (c) Sen. Rasheed Ladoja": "a",
            "10. Where is SQI located? (a)Ogbomoso (b)Kaduna (c)Kano": "a",
            "11. Who is the president of United States of America? (a)Joe Biden (b) Donald Trump (c)Putin": "a",
            "12. What is a young goat called? (a)Kid (b)Kitten (c)Puppy": "a",
            "13. How many continents do we have in the world? (a)6 (b)7 (c)8": "b",
            "14. Who is the founder of Facebook? (a)Elon Musk (b)Jeff Bezos(c)Mark Zuckerberg": "c",
            "15. What is the fastest means of transportation? (a)Road (b)Air (c)Sea": "b",
            "16. What club is the winner of 2024 UEFA Chamipions leauge (a)Real Madrid (b)Arsenal (c)PSG": "a",
            }

        for keys, value in test.items():
            print(keys)
            answer = input("Enter your answer: ")
            if answer == value:
                mark += 5
                print()
            else:
                print()
        print(f"Your total score is {mark} out of 80")
    else:
        print("Register to take the test")
    print()
showUs()


    


import mysql.connector as sql
myconnection=sql.connect(host="127.0.0.1", user="root", password="OldStunna27!", database="cbt_portal")
#print(myconnection)
mycursor=myconnection.cursor()
myconnection.autocommit=True
#mycursor.execute("CREATE DATABASE cbt_portal")
#mycursor.execute(" SHOW DATABASES ")
#for each in mycursor:
    #print(each)

#mycursor.execute("CREATE TABLE cbt_table(student_id INT(4) PRIMARY KEY AUTO_INCREMENT, name VARCHAR(25), matric_number VARCHAR(10), department VARCHAR(20), level VARCHAR(10), course_code VARCHAR(255) )")

#METHOD FOR NOT COLLECTING INPUT FOR USER
# my_query="INSERT INTO cbt_table(name, matric_number, department, level, course_code) VALUES(%s,%s,%s,%s,%s)"
# value=(("Pelumi Joshua", "2022001386", "Computer Science", "300 Level", "GNS301"))
# mycursor.execute(my_query, value)
# myconnection.commit()
# print(mycursor.rowcount, "record inserted")


student=2
list_of_students=[]
for i in range(student):
    name = input("Enter student name: ")
    matric_number = input("Enter matric number: ")
    department = input("Enter department: ")
    level = input("Enter level: ")
    course_code = input("Enter course code: ")

    # Prepare data tuple
    my_query="INSERT INTO cbt_table (name, matric_number, department, level, course_code) VALUES (%s,%s,%s,%s,%s)"
    value = (name, matric_number, department, level, course_code)

    try:
        # Execute the SQL query
        mycursor.execute(my_query, value)
        myconnection.commit()  # Commit the transaction
        print(f"{mycursor.rowcount} record(s) inserted.")
    except sql.Error as err:
        print(f"Error: {err}")
        myconnection.rollback()  # Rollback in case of error




# for i in range(student):

#     name=input("Enter your student name: ")
#     matric_number=input("Enter your matric number: ")
#     department=input("Enter your departmant: ")
#     level=input("Enter your level: ")
#     course_code=input("Enter course code: ")

# my_query="INSERT INTO cbt_table (name, matric_number, department, level, course_code) VALUES (%s,%s,%s,%s,%s)"
# value=(name, matric_number, department,level, course_code)

# mycursor.execute(my_query,value)
# #myconnection.commit()
# print(mycursor.rowcount, "records inserted")