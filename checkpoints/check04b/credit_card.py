"""
CS241 Check04B
Written by Chad Macbeth
"""

from address import Address

class CreditCard:
    def __init__(self):
        self.name = ""
        self.number = ""
        self.mailing_address = Address()
        self.billing_address = Address()

    def display(self):
        print(self.name)
        print(self.number)
      
        print("Mailing Address:")
        self.mailing_address.display()

        print("Billing Address:")
        self.billing_address.display()

