#creating a class

class MyClass:
    y = 8

# creating an object
p1 = MyClass()
print(p1.y)

#creating a class called "Person"
class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age

p1 = Person('Nemo', 6)

print(p1.name)
print(p1.age)

