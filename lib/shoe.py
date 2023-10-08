#!/usr/bin/env python3

class Shoe:
    def __init__(self, brand, size):
        self.brand = brand
        self.size = size

    @property
    def get_size(self):
        return self.size
    
    def set_size(self, size):
        if (type(size) in (int, float)):
            self.size = size
        else:
            print("size must be an integer\n")
        
    def cobble(self):
        self.condition = "new"
        print("Your shoe is as good as new!")

    