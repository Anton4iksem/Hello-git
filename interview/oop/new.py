number = 10
event = number % 2 == 0
print(event)

def factorial(n):
    return n * factorial(n-1)

# factorial(0)

import time


print(time.time())

class A:
    def __init__(self):
        self.x = 1
        self.__y = 1

    def getY(self):
        return self.__y
a = A()
a.x = 45
print(a.x)


x = True
y = False
z = False

if not x or y:
    print(1)
elif not x or not y and z:
    print(2)
elif not x or y or not y and x:
    print(3)
else:
    print(4)


class Parent():
    def __init__(self, param):
        self.v1 = param

class Child(Parent):
    def __init__(self, param):
        super().__init__(param=14)
        self.v2 = param

obj = Child(11)
print("%d %d" % (obj.v1, obj.v2))


counter = 1

def a():
    global counter
    for i in (1, 2, 3):
        counter += 1

a()
print(counter)


class A:
    def __str__(self) -> str:
        return "A"

class B(A):
    def __init__(self) -> None:
        super().__init__()

class C(B):
    def __init__(self) -> None:
        super().__init__()

def maim():
    b = B()
    a = A()
    c = C()
    print(a, b, c)

maim()

x = 2 
y =1 
x *= y + 1
print(x)

nums = set([1, 1, 2, 3, 3, 3, 4])
print(len(nums))

def f1 (x = 1, y = 2):
    x = x + y
    y += 1
    print(x, y)

f1(y = 2, x = 1)

my_list = [1, 5, 5, 5, 5, 1]
max_ = my_list[0]
# index_of_max = 0
for i in range(1, len(my_list)):
    if my_list[i] > max_:
        max_ = my_list[i]
        index_of_max = i
print(index_of_max)