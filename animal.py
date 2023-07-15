from abc import ABC, abstractmethod

class Animal(ABC):
    @abstractmethod
    def eat(self):
        pass

    @abstractmethod
    def sleep(self):
        pass

class Lion(Animal):
    def eat(self):
        print("Lion is eating.")

    def sleep(self):
        print("Lion is sleeping.")

class Tiger(Animal):
    def eat(self):
        print("Tiger is eating.")

    def sleep(self):
        print("Tiger is sleeping.")

class Deer(Animal):
    def eat(self):
        print("Deer is eating.")

    def sleep(self):
        print("Deer is sleeping.")

# Create instances of the subclasses
lion = Lion()
tiger = Tiger()
deer = Deer()

# Call the eat() and sleep() methods on the instances
lion.eat()   # Output: Lion is eating.
lion.sleep() # Output: Lion is sleeping.

tiger.eat()   # Output: Tiger is eating.
tiger.sleep() # Output: Tiger is sleeping.

deer.eat()   # Output: Deer is eating.
deer.sleep() # Output: Deer is sleeping.
