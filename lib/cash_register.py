#!/usr/bin/env python3

class CashRegister:
    def __init__(self, discount=0):
        # Initialize CashRegister with an optional discount, defaulting to 0.
        self.discount = discount
        self.total = 0
        self.items = []
        self.previous_transactions = []

    def add_item(self, item, price, quantity=1):
        # Add an item to the register with a specified price and optional quantity.
        self.total += price * quantity
        # Add the item to the items list based on the specified quantity.
        self.items.extend([item] * quantity)
        # Record the transaction details in the previous_transactions list.
        self.previous_transactions.append({"item": item, "quantity": quantity, "price": price})

    def apply_discount(self):
        # Apply a discount to the total if a discount is set.
        if self.discount:
            self.total = int(self.total * (1 - self.discount / 100))
            print(f"After the discount, the total comes to ${self.total}.")
        else:
            print("There is no discount to apply.")

    def void_last_transaction(self):
        # Void the last transaction by subtracting its cost from the total.
        if not self.previous_transactions:
            return "There are no transactions to void."
        last_transaction = self.previous_transactions.pop()
        self.total -= last_transaction["price"] * last_transaction["quantity"]
        # Remove the items from the items list based on the last transaction's quantity.
        self.items = self.items[:-last_transaction["quantity"]]
       