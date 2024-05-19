#!/usr/bin/env python3

class CashRegister:
    def __init__(self, discount = 0):
        self.discount = discount
        self.total = 0
        self.items = []
        self.last_trans = 0
        
    def add_item(self, title, price, quantity = 1):
        for _ in range(quantity):
            self.items.append(title)
        self.total += price * quantity
        self.last_trans = price * quantity
  
    def apply_discount(self):
        if self.discount == 0:
            print("There is no discount to apply.")
        else:
            discount_amount = self.total * (self.discount / 100)
            self.total -= discount_amount
            total = int(self.total)
            print(f"After the discount, the total comes to ${total}.")

    def void_last_transaction(self):
        if not self.items:
            print("No transactions to void.")
            return
        last_amount = self.last_trans
        self.total -= last_amount
        last_item = self.items.pop()
        print(f"Last transaction with item '{last_item}' of ${last_amount} has been voided.")
