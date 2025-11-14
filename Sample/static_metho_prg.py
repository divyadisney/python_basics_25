

# static  method
"""
class ShoppingCart:
    def __init__(self, customer_name):
        self.customer_name = customer_name
        self.items = []  # list of (item_name, price)

    def add_item(self, item_name, price):
        self.items.append((item_name, price))

    def total_amount(self):
        return sum(price for _, price in self.items)

    @staticmethod
    def calculate_discount(amount):
        # A static method that applies discount based on total amount.
        if amount >= 5000:
            return amount * 0.10   # 10% discount
        elif amount >= 2000:
            return amount * 0.05   # 5% discount
        else:
            return 0

    def final_amount(self):
        total = self.total_amount()
        discount = ShoppingCart.calculate_discount(total)
        return total - discount


# --- Example Usage ---
cart1 = ShoppingCart("Anna")
cart1.add_item("Laptop", 45000)
cart1.add_item("Mouse", 1000)

print("Customer:", cart1.customer_name)
print("Total Amount: ₹", cart1.total_amount())
print("Discount: ₹", cart1.calculate_discount(cart1.total_amount()))
print("Final Payable Amount: ₹", cart1.final_amount())"""
# class method
from datetime import date

class Student:
    school_name = "ABC School"

    def __init__(self, name, age):
        self.name = name
        self.age = age

    @classmethod
    def from_dob(cls, name, birth_year):
        """Create a Student object using date of birth (year)."""
        current_year = date.today().year
        age = current_year - birth_year
        return cls(name, age)  # creates a new Student object

    def display(self):
        print(f"Name: {self.name}, Age: {self.age}, School: {Student.school_name}")
# Creating student by giving age directly
s1 = Student("Anna", 20)

# Creating student using date of birth (class method)
s2 = Student.from_dob("John", 2005)

s1.display()
s2.display()

