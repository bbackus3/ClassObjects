#define a class 
class Animal: #'animal' is the name of the class 
    name = ""
    species = 0  #name/species are the variable inside the class with set values 

animal1 = Animal() #creating an object of the class

animal1.name = 'manatee'
animal1.species = 'aquatic mammal'

print(f"Name: {animal1.name}, Species: {animal1.species}")
#the two attributes are name and species 
#the object is animal

#creating multiple objects of a class
class Character:
    character_name = 0 

character_name1 = Character()
character_name2 = Character()

character_name1.character_name = 'figment'
character_name2.character_name = 'olaf'

print(f'the first character is: {character_name1.character_name}')
print(f'the second character is: {character_name2.character_name}')


#calculating inside something 

class Office:
    length = 0.0
    width = 0.0

    def calculate_length_width(room): #'calculate_length_width' is the method
        print("The length plus the width of the room is = ", room.length + room.width)

#creating an object of the office
desk = Office()

desk.length = 3
desk.width = 6

desk.calculate_length_width() #the '.' notation calls the method

#PYTHON CONSTRUCTORS
class Animal:
    def __init__(what, name = ''):
        what.name = name

animal1 = Animal()
animal1 = Animal('manatee')

#PYTHON INHERITANCE

class Animal:
    type = ''

    def diet(self):
        print('a manatees diet is eating vegetation', self.type)

class Manatee(Animal):
    def display(self):
        #this is how to access an attribute of superclass using 'self'
        print('My favorite animal is a', self.name)

manatee = Manatee() #this creates an object of the subclass

manatee.name = 'Manatee' #manatee.diet and manatee.name is access to the superclass attribute and method 
manatee.diet()

manatee.display() #calling the subclass method

#define a polygon class in order to find out the area of a pentagon
class Polygon:
    def __init__(shape, num_of_sides):
        shape.num = num_of_sides
        shape.sides = [0 for i in range(num_of_sides)]

    def SidesCount(shape):
        shape.sides = [float(input("what side" + str(i+1)+ " : "))for i in range(shape.num)]

    def WhatSides(shape):
        for i in range(shape.num):
            print("Side", i+1, "is", shape.sides[i])
                       


class Pentagon(Polygon):
    def __init__(shape):
        Polygon.__init__(shape, 5) #5 is for the # of sides

    def findArea(shape):
        a, b, c, d, e = shape.sides
        s = (a + b + c + d + e)/ 2
        area = (s*(s-a)*(s-b)*(s-c)*(s-d)*(s-e)) ** 0.5
        print('the area of the pentagon is %0.2f' %area)

p = Pentagon() #this creates an object of the subclass
p.SidesCount() #p.SidesCount and p.WhatSides is access to the superclass attribute and method 
p.WhatSides()
p.findArea() #calls the subclass method 


#METHOD OVERRIDING
class Animal:
    type = ''

    def diet(self):
        print('a manatees diet is eating vegetation')

class Manatee(Animal):
    def eat(self):
        print('manatees dont eat meat')

manatee = Manatee() #this creates an object of the subclass
manatee.eat()

#MULTIPLE INHERITANCE

#features of a superclass 
class SuperClass1:
class SuperClass2:

#features of (SuperClass1 + SuperClass2 + MultiDerived class) which equals a multiple inheritance
class MultiDerived(SuperClass1, SuperClass2):

#example: mammal + herbivore = manatee (a manatee is BOTH a mammal and herbivore)

class Mammal: 
    def what_mammal(animal):
        print('my favorite mammal is a manatee')

class Herbivore:
    def diet(animal):
        print('my favorite mammal is a herbivore')

class Manatee(Mammal, Herbivore):
    pass #pass is a placeholder for future code (avoids potential errors when there is empty code)

m = Manatee()

#calling the method
m.what_mammal()
m.diet()






