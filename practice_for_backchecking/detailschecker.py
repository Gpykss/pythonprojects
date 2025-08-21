

# def name_checker(classin, a , b, username = 0, age=10):
#     print(f"hello {username}")
#     print(f"you are in {classin}")
#     print(f"you are {age} years old")
#     name  = a + b
#     return name
#
#
#
#
# print(name_checker(5,6,7))
# print(name_checker(0,0,0,4,5))

def numbers(*num):
 for number in num:
     number += 1
     print(number)

print(numbers(6,6,7,8,9,6,5))


def bio(**kwargs):
    for key,value in kwargs.items():
        print(f'the key is {key} and the value is {value}')

bio(name="mr. Gift", age ="10",city="rivers state",DOB= "16/07/2025")



#list comprehension
grades = range(1,10)

passing_grades =[num for num  in grades if num >= 5]
