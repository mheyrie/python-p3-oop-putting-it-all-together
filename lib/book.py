#!/usr/bin/env python3

class Book:
    def __init__(self, title, page_count ):
        self.title = title
        self.page_count = page_count
        pass
    
    @property
    def get_page_count(self):
        return self.page_count
    
    def set_page_count(self, page_count):
        if (type(page_count) in (int, float)):
            return page_count
        else:
            print("page_count must be an integer\n.")

    def turn_page(self):
        print("Flipping the page...wow, you read fast!")
           