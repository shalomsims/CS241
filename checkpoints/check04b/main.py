"""
CS241 Checkpoint 4B
Written by Chad Macbeth
"""

from address import Address
from credit_card import CreditCard

def main():
    cc = CreditCard()

    cc.name = input("Name: ")
    cc.number = input("Number: ")
    
    print("Mailing Address:")
    cc.mailing_address.street = input("Street: ")
    cc.mailing_address.city = input("City: ")
    cc.mailing_address.state = input("State: ")
    cc.mailing_address.zip = input("Zip: ")
    
    print("Billing Address:")
    cc.billing_address.street = input("Street: ")
    cc.billing_address.city = input("City: ")
    cc.billing_address.state = input("State: ")
    cc.billing_address.zip = input("Zip: ")

    cc.display()

if __name__ == "__main__":
    main()
