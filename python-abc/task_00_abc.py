#!/usr/bin/python3
from abc import ABC, abstractmethod

class Animal(ABC):
    """Abstract base class for animals."""
    
    @abstractmethod
    def sound(self):
        """Return sound"""
        pass

class Dog(Animal):
    """ dog"""
    
    def sound(self):
        return "Bark"

class Cat(Animal):
    """Represents a cat"""
    
    def sound(self):
        return "Meow"

if __name__ == "__main__":
    dog = Dog()
    cat = Cat()

    print(f"The dog says: {dog.sound()}")
    print(f"The cat says: {cat.sound()}")
