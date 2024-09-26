#!/usr/bin/python3
from abc import ABC, abstractmethod
class Animal(ABC):
    def sound(self):
        
class Dog(Animal):
    
    def sound(self):
        return "Bark"

class Cat(Animal):
    
    def sound(self):
        return "Meow"