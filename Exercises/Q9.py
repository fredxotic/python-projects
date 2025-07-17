class Restaurant:
    def __init__(self, restaurant_name, cuisine_type):
        self.restaurant_name = restaurant_name
        self.cuisine_type = cuisine_type
        self.number_served = 0

    def describe_restaurant(self):
        print(f"\nWelcome to {self.restaurant_name}.")
        return f"\t{self.restaurant_name} offers {self.cuisine_type}."

    def open_restaurant(self):
        print(f"\tThe {self.restaurant_name} is now open!")

    def count_customers(self):
        print(f"\tServed: {self.number_served} customers.\n")
    
    def set_number_served(self, number):
        self.number_served = number
        print("\tCustomers Served:", number)
    
    def increment_number_served(self, customers_served):
        self.number_served = self.number_served + customers_served
        print("\tCustomers Served:", self.number_served)
        
class IceCreamStand(Restaurant):
    def __init__(self, restaurant_name, cuisine_type):
        super().__init__(restaurant_name, cuisine_type)
        self.flavors = ['vanilla','banana','strawberry','chocolate']

    def available_flavours(self):
        print("\tThe Ice cream Flavors available are:")
        for flav in self.flavors:
            print(f"\t\t{flav.title()}")





