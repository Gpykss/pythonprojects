import csv
import json
import os
from sys import exception



# file1 = "C:/Users/GODSPOWER/PycharmProjects/PythonProject1/filedet.txt"
# file2 = "C:/Users/GODSPOWER/PycharmProjects/PythonProject1/creative"
# file3 = "C:/Users/GODSPOWER/Desktop/test.txt"
# file4 = "C:/Users/GODSPOWER/Desktop"
#
#
# if os.path.exists(file2) :
#     print("there all exists ")
#
# else:
#     print("there are not files ")
#
# if os.path.isfile(file1):
#     print("this is a file ")
# else:
#     print("This is not a file ")
#
# if os.path.isdir(file2):
#     print("this is a Directory ")
# else:
#     print("This is not a Directory ")
grade_name = {
    "godspower" : 10,
    "john ": 40,
    "alicia" :50
}
cv_name =[["name ","age"],
          ["Godspower",20],
          ["john", 10]]
myName = "name.json"
myNamet = "name.txt"
csv_name = "name.csv"
text = "this is my first file"
append_text = "this is the added text "
# students = []
# student_name = input("What is your name: \n")
# students.append(student_name)
# print("student added ")

# try:
#     with open(myNamet,"a") as file:
#         file.write(append_text + "\n")
#         print(" file creted ")
# except Exception:
#     print("Something Went wrong")
#
# try:
#     with open(myName,"w") as file:
#         # file.write(myName)
#         json.dump(grade_name,file, indent= "    " )
#         print(" file creted ")
# except Exception:
#     print("Something Went wrong")
#
# try:
#     with open(csv_name, "w" , newline="") as file:
#         writer = csv.writer(file)
#         for row in  cv_name:
#             writer.writerow(row)
#         print("csv file created")
# except Exception:
#     print("PLease check the code you wrote ")

#to read a fil


with open(myName, "r")  as file :
    content = json.load(file)
    print(content["godspower"])

with open(myNamet, "r")  as file :
    content = file.read()
    print(content)

with open(csv_name, "r")  as file :
    content = csv.reader(file)
    for line in content:
        print(line[0])