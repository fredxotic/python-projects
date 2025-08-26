# Assignment 1: Design the Class (with Inheritance) ---

class Vehicle:
    def __init__(self, make, model):
        self.make = make
        self.model = model

    def move(self):
        print("This vehicle is moving.")

    def display_info(self):
        print(f"Vehicle: {self.make} {self.model}")

class Car(Vehicle):
    def __init__(self, make, model, color):
        super().__init__(make, model)
        self.color = color

    # --- Assignment 2: Polymorphism Challenge! ---
    def move(self):
        print(f"Driving the {self.color} {self.model}.")

    def display_info(self):
        print(f"Car: {self.color} {self.make} {self.model}")

class Plane(Vehicle):
    def __init__(self, make, model, seats):
        super().__init__(make, model)
        self.seats = seats

    # Assignment 2: Polymorphism Challenge!
    def move(self):
        print(f"Flying the {self.model}.")

    def display_info(self):
        print(f"Plane: {self.make} {self.model} with {self.seats} seats")


# --- Main program to demonstrate ---
if __name__ == "__main__":
    
    my_car = Car("Ford", "Mustang", "Red")
    my_plane = Plane("Airbus", "A380", 853)
    
    print("--- Vehicle Information ---")
    my_car.display_info()
    my_plane.display_info()
    print("-" * 25)
    
    print("\n--- Demonstrating Polymorphism ---")
    vehicles = [my_car, my_plane]
    
    for vehicle in vehicles:
        vehicle.move()
