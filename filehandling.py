# todo_list=open("todo_app.txt", "w")
# todo_list.write("This is a to do list app")
# print("done")

# with open("todo_app.txt", "a") as todo_list:
#     todo_list.write(" This is for the day to day activities")
#     print("appended to file")
# todo_list=open("todo_app.txt", "r")
# todo_list.read()

import os
os.mkdir("/Users/oldstunna/Documents/Week_16/python_practice/new_file.txt")
print("done")

new_file=open("new_file.txt", "w")
new_file.write("This is a new path creating a new directory")
print(new_file.read())
print("done")


