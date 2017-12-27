"""
CS241 Checkpoint 04B
Written by Chad Macbeth
"""

class Address:
    def __init__(self):
        self.street = ""
        self.city = ""
        self.state = ""
        self.zip = ""

    def display(self):
        print(self.street)
        print("{}, {} {}".format(self.city, self.state, self.zip))


