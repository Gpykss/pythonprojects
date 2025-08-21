class numbers:
    def __init__(self,x,y):
        self._x = x
        self._y = y

    def __add__(self, other):
        return self._x + other

    def __lt__(self, other):
        return self._x < other

    def __gt__(self, other):
        return self._x > other

    @property
    def x(self):
        return self._x

    @x.setter
    def x(self,new_x):
        self._x = new_x

    @x.deleter
    def x(self):
        del self._x
        print("deleted")

case1 = numbers(6,8)
case2 =numbers(10,9)

case1.x = 10
del case1.x


# print(case1.x)
# print(case1._x + case1._y)
# print(case1._x > case2._y)


#decorators syntax below
# def addname (func):
#     def wrapper():
#         func()
#     return wrapper()

def addname (func):
    def wrapper(*args,**kwargs):
        print("cold berry Icecream")
        func(*args,**kwargs)
    return wrapper

@addname
def ff(flavor):
    print(f"the flavor is {flavor}")

ff("coldberry")

# exceptioins

try:
    firstName = input("Your First name: ")
    lastNmae = input("Your last name: ")
    fullName = firstName +lastNmae
    print(fullName)
except ValueError:
    print("Value error")
except TypeError:
    print("type error")
except ZeroDivisionError:
    print("zero divisin error")

