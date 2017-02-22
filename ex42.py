## Animal is-a object
class Animal(object):
    pass

## Dig is-a Animal
class Dog(Animal):

    def __init__(self, name):
        ## Dog has-a function __init__ that takes self and name as parameters
        self.name = name

## Cat is-a Animal
class Cat(Animal):

    def __init__(self, name):
        ## Cat has-a function __init__ that takes self and name as parameters
        self.name = name
## Person is-a object
class Person(object):

    def __init__(self, name):
        ## Person has-a function __init__ that takes self, name as parameters
        self.name = name
        self.pet = None

## Employee is-a Person
class Employee(Person):
    def __init__(self, name, salary):
        ##??
        super(Employee, self).__init__(name)
        ## from self get the attribute salary and set it to salary
        self.salary = salary

## Fish is-a object
class Fish(object):
    pass

class Salmon(Fish):
    pass

class Halibut(Fish):
    pass

rover = Dog("Rover")

satan = Cat("Satan")

mary = Person("Mary")

mary.pet = satan

frank = Employee("Frank", 120000)

frank.pet = rover

flipper = Fish()

crouse = Salmon()

harry = Halibut()
