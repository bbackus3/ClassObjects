#creating a class

class MyClass:
    y = 8

# creating an object
p1 = MyClass()
print(p1.y)

#creating a class called "Animal"
#age(months)
class Animal:
    def __init__(self, name, age):
        self.name = name
        self.age = age

p1 = Animal('Nemo', 6)

print(p1.name)
print(p1.age)

#can call the "self" parameter whatever you want
class Animal:
    def __init_(mypet, name, age):
        mypet.name = name
        mypet.age = age

    def myfunc(abc):
        print('My cats name is ' + abc.name)

#p1 = Animal('Nemo', 6)
p1.myfunc()

#how to modify object properties 
p1.age = 8

#deleting object properties
del p1.age

#deleting objects 
del p1

class Person:
    pass

#creating a parent class
class Person:
    def __init__(self, fname, lname):
        self.firstname = fname
        self.lastname = lname

    def printname(self):
        print(self.firstname, self.lastname)

#can create an object with the person class
b = Person('Nemo', 'Dusky')
b.printname()

#creating a child class 
class Student(Person):
    pass

x = Student("Taylor", "Swift")
x.printname()

class Student(Person):
    def __inti__(self, fname, lname):
        super().__init__(fname, lname)

#adding a property to the sudent class
class Student(Person):
    def __init__(self, fname, lname):
        super().__init__(fname, lname)
        self.graduation_year = 2018

x = Student("Taylor", "Swift", 2018)

#overwritting the parent method 
class Student(Person):
    def __init__(self, fname, lname, year):
        super().__init__(fname, lname)
        self.graduation_year = year

    def welcome(self):
        print("Welcome", self.firstname, self.lastname, "to the class of", self.graduation_year)





