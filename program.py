class Item:

    def __init__(self, name, price, quantity):
        self.name = name
        self.price = price
        self.quantity = quantity

    def total_price(self):
        return self.price * self.quantity


class ShoppingCart:

    def __init__(self):
        self.items = []

    # Add item
    def add(self, name, price, quantity):
        item = Item(name, price, quantity)
        self.items.append(item)

    # Calculate subtotal
    def subtotal(self):
        return sum(item.total_price() for item in self.items)

    # Apply discount
    def discount(self, percentage):
        return self.subtotal() * percentage / 100

    # Calculate tax
    def tax(self, percentage):
        amount_after_discount = self.subtotal() - self.discount(percentage)
        return amount_after_discount * 18 / 100

    # Calculate final amount
    def final_amount(self, discount_percentage):
        subtotal = self.subtotal()
        discount = self.discount(discount_percentage)
        tax = (subtotal - discount) * 18 / 100

        return subtotal - discount + tax

    # Remove item
    def remove_item(self, name):
        self.items = [
            item for item in self.items
            if item.name != name
        ]

    # Display cart
    def display(self):
        print("\nItems in Cart:")

        for item in self.items:
            print(
                item.name,
                "Price:", f"₹{item.price:.2f}",
                "Quantity:", item.quantity,
                "Total:", f"₹{item.total_price():.2f}"
            )


# Create shopping cart
cart = ShoppingCart()

# Add items
cart.add("Laptop", 50000, 1)
cart.add("Mouse", 1000, 2)
cart.add("Keyboard", 2000, 1)

# Display items
cart.display()

# Calculate subtotal
subtotal = cart.subtotal()

# Apply 10% discount
discount = cart.discount(10)

# Calculate GST
tax = cart.tax(10)

# Calculate final amount
final = cart.final_amount(10)

print("\n----- BILL -----")
print("Subtotal:", f"₹{subtotal:.2f}")
print("Discount:", f"₹{discount:.2f}")
print("GST (18%):", f"₹{tax:.2f}")
print("Final Amount:", f"₹{final:.2f}")


# Payment processing simulation
print("\nPayment Processing...")

payment_successful = True

if payment_successful:
    print("Payment Successful!")
    print("Order Confirmed")
    print("Order Status: Placed")
else:
    print("Payment Failed")


# Remove an item
cart.remove_item("Mouse")

print("\nAfter Removing Mouse:")
cart.display()