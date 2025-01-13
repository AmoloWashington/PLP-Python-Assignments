class Smartphone:
    def __init__(self, brand, model, price):
        self.brand = brand
        self.model = model
        self.price = price

    def display_info(self):
        return f"{self.brand} {self.model} costs ${self.price}"

    def call(self, number):
        return f"Calling {number} from {self.model}..."

class Smartwatch(Smartphone):
    def __init__(self, brand, model, price, battery_life):
        super().__init__(brand, model, price)
        self.battery_life = battery_life

    def display_info(self):
        return f"{self.brand} {self.model} (Smartwatch) with {self.battery_life} hours of battery life costs ${self.price}"

    def track_fitness(self):
        return f"Tracking fitness on {self.model}..."

phone = Smartphone("Apple", "iPhone 14", 999)
watch = Smartwatch("Samsung", "Galaxy Watch 6", 399, 48)

print(phone.display_info())
print(watch.display_info())
print(watch.track_fitness())

