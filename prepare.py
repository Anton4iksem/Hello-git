def foo(a=[]):
    a.append(1)
    print(a)

foo()
foo()
foo()

class ObjectCreator(object):
   pass

my_object = ObjectCreator()
print(my_object)

class SomeClass(object):
    attr1 = 42

    def method1(self, x, y):
        return 2*x*y

obj = SomeClass()
print(obj.method1(6,2)) 
print(obj.attr1) 

class Point(object):
    def __init__(self, x, y, z):
        self.coord = (x, y, z)

p = Point(13, 14, 15)
print(p.coord)

class SomeClass(object):
    pass

def squareMethod(self, x):
    return x*x

SomeClass.square = squareMethod
obj = SomeClass()
print(obj.square(5)) 

class SomeClass(object):
    @staticmethod
    def hello():
        print("Hello, world")

SomeClass.hello() # Hello, world
obj = SomeClass()
obj.hello() # Hello, world


class SomeClass(object):
    @classmethod
    def hello(cls):
        print('Hello, класс {}'.format(cls.__name__))

SomeClass.hello() # Hello, класс SomeClass

class SomeClass:
    def _private(self):
        print("Это внутренний метод объекта")

obj = SomeClass()
obj._private() # это внутренний метод объекта

class SomeClass():
    def __init__(self):
        self.__param = 42 # защищенный атрибут

obj = SomeClass()
# obj.__param # AttributeError: 'SomeClass' object has no attribute '__param'
print(obj._SomeClass__param) # 42

class SomeClass():
    def __init__(self, value):
        self._value = value

    def getvalue(self): # получение значения атрибута
        return self._value

    def setvalue(self, value): # установка значения атрибута
        self._value = value

    def delvalue(self): # удаление атрибута
        del self._value

    value = property(getvalue, setvalue, delvalue, "Свойство value")

obj = SomeClass(42)
print(obj.value)


class Mammal():
    className = 'Mammal'

class Dog(Mammal):
    species = 'Canis lupus'

dog = Dog()
print(dog.className, dog.species) # Mammal

class Horse():
    isHorse = True

class Donkey():
    isDonkey = True

class Mule(Horse, Donkey):
    pass 

mule = Mule()
print(mule.isHorse) # True
print(mule.isDonkey) # True

# композиция 

class Salary:
    def __init__(self,pay):
        self.pay = pay

    def getTotal(self):
        return (self.pay*12)

class Employee:
    def __init__(self,pay,bonus):
        self.pay = pay
        self.bonus = bonus
        self.salary = Salary(self.pay) # !!!

    def annualSalary(self):
        return "Total: " + str(self.salary.getTotal() + self.bonus)

employee = Employee(100,10)
print(employee.annualSalary())

# агрегация 

class Salary(object):
    def __init__(self, pay):
        self.pay = pay

    def getTotal(self):
        return (self.pay * 12)

class Employee(object):
    def __init__(self, pay, bonus):
        self.pay = pay
        self.bonus = bonus

    def annualSalary(self):
        return "Total: " + str(self.pay.getTotal() + self.bonus) # !!!

salary = Salary(100)
employee = Employee(salary, 10)
print(employee.annualSalary())