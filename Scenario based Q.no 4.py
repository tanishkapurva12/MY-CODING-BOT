class Mobile:
    def __init__(self, brand, model, price):
        self.brand = brand
        self.model = model
        self.price = price
        self.category = self.get_category()

    def get_category(self):
        if self.price >= 50000:
            return "Premium"
        elif self.price >= 20000:
            return "Mid-range"
        else:
            return "Budget"


class Store:
    def __init__(self):
        self.mobiles = []

    def add_mobile(self, mobile):
        self.mobiles.append(mobile)
        print("Mobile added successfully.")

    def display_mobiles(self):
        print("\n===== Mobile Store =====")

        if not self.mobiles:
            print("No mobiles available.")
            return

        for mobile in self.mobiles:
            print("Brand:", mobile.brand)
            print("Model:", mobile.model)
            print("Price: ₹", mobile.price)
            print("Category:", mobile.category)
            print("------------------------")


# Create Store object
store = Store()

while True:
    print("\n===== Mobile Store Management System =====")
    print("1. Add Mobile")
    print("2. Display All Mobiles")
    print("3. Exit")

    choice = input("Enter your choice: ")

    if choice == "1":
        brand = input("Enter mobile brand: ")
        model = input("Enter mobile model: ")
        price = float(input("Enter mobile price: ₹"))

        mobile = Mobile(brand, model, price)
        store.add_mobile(mobile)

    elif choice == "2":
        store.display_mobiles()

    elif choice == "3":
        print("Thank you for using Mobile Store Management System.")
        break

    else:
        print("Invalid choice. Please try again.")
