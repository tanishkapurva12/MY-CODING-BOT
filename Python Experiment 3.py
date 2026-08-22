from abc import ABC, abstractmethod
# Strategy Interface
class PaymentStrategy(ABC):
    @abstractmethod
    def pay(self, amount):
        pass
# Concrete Strategy 1: Credit Card
class CreditCardPayment(PaymentStrategy):
    def pay(self, amount):
        print(f"Paid ₹{amount} using Credit Card")
# Concrete Strategy 2: UPI
class UPIPayment(PaymentStrategy):
     def pay(self, amount):
        print(f"Paid ₹{amount} using UPI")
# Concrete Strategy 3: PayPal
class PayPalPayment(PaymentStrategy):
    def pay(self, amount):
        print(f"Paid ₹{amount} using PayPal")
# Context
class PaymentProcessor:
    def __init__(self, strategy):
        self.strategy = strategy
    def set_strategy(self, strategy):    
        self.strategy = strategy
    def process_payment(self, amount):
        self.strategy.pay(amount)
# Main Program
print("Select Payment Method:")
print("1. Credit Card")
print("2. UPI")
print("3. PayPal")
choice = int(input("Enter your choice: "))
amount = float(input("Enter payment amount: ₹"))

if choice == 1:
    strategy = CreditCardPayment()
elif choice == 2:
    strategy = UPIPayment()
elif choice == 3:
    strategy = PayPalPayment()
else:
    print("Invalid payment method")
    exit()
processor = PaymentProcessor(strategy)
processor.process_payment(amount)
