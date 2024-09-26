#!/usr/bin/python3
from abc import ABC, abstractmethod

class Shape(ABC):

@abstractmethod
    def area(self):
        """area"""
        pass

    @abstractmethod
    def perimeter(self):
        """perimeter"""
        pass

class Circle(Shape):
    """a circle"""
    
    def __init__(self, radius):
        self.radius = radius
    
    def area(self):
        return 3.14 * self.radius ** 2
    
    def perimeter(self):
        return 2 * 3.14 * self.radius

class Rectangle(Shape):
    """a rectangle"""
    
    def __init__(self, width, height):
        self.width = width
        self.height = height
    
    def area(self):
        return self.width * self.height
    
    def perimeter(self):
        return 2 * (self.width + self.height)