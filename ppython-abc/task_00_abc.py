#!/usr/bin/python3

from abc import ABC, abstractmethod


class Animal(ABC):
    """
    Define the abstract base class
    """
    @abstractmethod
    def sound(self):
        pass


class Dog(Animal):
    """Define the Dog subclass
    """
    def sound(self):
        return "Bark"


class Cat(Animal):
    """
    Define the cat subclass
    """
    def sound(self):
        return "Meow"
