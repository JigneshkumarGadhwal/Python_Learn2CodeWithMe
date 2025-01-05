# Prevents user from creating an object of that class.
# + compels a user to override abstract methods in a child class

#Abstract class = a class which contains onw or more abstract methods.
# abstract method  =  a method that has a declaration but does not have an implementation.
#
# class Vehicle:
#     def go(self):
#         pass
# class Car(Vehicle):
#
#     def go(self):
#         print("You drive the car")
#
# class Motorcycle(Vehicle):
#     def go(self):
#
#         print("You ride the motorcycle")
#
# vehicle = Vehicle()
# car = Car()
# motorcycle = Motorcycle()
#
# vehicle.go()
# car.go()
# motorcycle.go()

# When we run this, go method within the vehicle class wil not be executed since we did not define
# anything for that.

#Suppose we need user to create an object using the child class. one way in which we can prvent
# the user to create an object of the parent class to turn parent in to abstract class

# for that, we need some imports:
# abc = Abstract based class

from abc import ABC,abstractmethod
class Vehicle(ABC):
    # Now we are going to add this decorator.
    @abstractmethod
    def go(self):
        pass
class Car(Vehicle):

    def go(self):
        print("You drive the car")

class Motorcycle(Vehicle):
    def go(self):

        print("You ride the motorcycle")

vehicle = Vehicle()
car = Car()
motorcycle = Motorcycle()

vehicle.go()
car.go()
motorcycle.go()




