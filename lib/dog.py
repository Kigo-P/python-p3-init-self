#!/usr/bin/env python3

class Dog:
    
    def __init__(self, name, breed = "Mutt"):
        self.name = name
        self.breed = breed
    pass


hulk = Dog("hitler")
print(hulk.name)
print(hulk.breed)
