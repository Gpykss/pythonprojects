# # class shapes :
# #     def __init__(self,color):
# #         self.color =color
# #
# #     def desc(self):
# #         print("great "if self.color == "blue" else "no " )
# #
# # class square(shapes):
# #     def __init__(self,color,name):
# #         self.name = name
# #         super().__init__(color)
# #
# #     def checker(self):
# #         super().desc()
# #
# #
# # class circle(shapes):
# #     def __init__(self,color,name):
# #         super().__init__(color)
# #         self.name = name
# #
# #     def checker(self):
# #         super().desc()
# #
# #
# # class triangle(shapes):
# #     def __init__(self,color,name):
# #         super().__init__(color)
# #         self.name = name
# #
# #     def checker(self):
# #         super().desc()
# #
# #
# #
# # square = square("blue" , "square")
# # circle = circle("pink" , "square")
# # triangle = triangle("green" , "square")
# #
# #
# #
# # print(square.name)
# # print(square.color)
# #
# # print()
# #
# # print(triangle.name)
# # print(triangle.color)
# #
# #
# # print()
# #
# # square.checker()
# # circle.checker()
# # triangle.checker()
# #
# # print()
# #
# # print(circle.name)
# # print(circle.color)
#
#
# #static method
# class names:
#     def __init__(self,firstname,lastname):
#         self.firstname =firstname
#         self.lastname = lastname
#
#
#     def displayName(self):
#
#         return f"{self.firstname} {self.lastname}"
#
#     @staticmethod
#     def nameValid(namelen):
#         if len(namelen) >= 15:
#             print("your name is invalid please input less than 15")
#         else:
#             print("your name is valid")
#
#
# user1 = names("grace", "joseph")
# user2 = names("peace", "Godspowers")
# user3 = names("john", "gift")
#
#
# print(user1.displayName())
# print(user2.displayName())
# print(user3.displayName())
# print(names.nameValid(user1.displayName()))
# print(names.nameValid(user2.displayName()))
# print(names.nameValid(user3.displayName()))
#
#
# class checking:
#     def __init__(self,date,time):
#         self.date = date
#         self.time = time
#
#     def honk(self):
#         print("honk")
#
# class sub1(checking):
#     def __init__(self,date,time):
#         super().__init__(date,time)
#
# class sub2:
#     def honk(self):
#         print("honk")
#
#
# names =[sub1(18,19), sub2()]
#
# for name in names:
#     name.honk()
#

#class maethd allows operaiton related to classs
class students:

    count = 0
    total_gpa =0

    def __init__(self,name,gpa):
        self.name = name
        self.gpa = gpa
        students.count +=1
        students.total_gpa += gpa

    def display(self):
        return f"{self.name}  {self.gpa}"

    @classmethod
    def getinfo(cls):
        if cls.count == 0:
            return f'Sorry no data'
        else:
            return f"{cls.total_gpa / cls.count : .2f}"

user1 = students("godspower", 3.5)
user2 = students("john", 3)

print(f"Hello {user1.name} your GPA is {user1.gpa}")
print(f"Hello {user2.name} your GPA is {user2.gpa}")
print(students.getinfo())