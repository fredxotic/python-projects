class Car:
    def __init__(self, make, model, year):
        self.make = make
        self.model = model
        self.year = year
        self.odometer_reading = 0                                   #setting a Default Value for an attribute
    
    def get_descriptive_name(self):
        formatted_name = f"{self.year} {self.make} {self.model}"
        return formatted_name.title()
    
    def read_odometer(self):                                        #Setting a default Value to an attribute
        print(f"This car has {self.odometer_reading} miles on it.")

    def update_odometer(self, mileage):                             #Modifying an attribute's Value Through a Method 
        if mileage >= self.odometer_reading:
            self.odometer_reading = mileage
        else:
            print("You can't roll back an odometer.")

    def increment_odometer(self, miles):                            #incrementing an attribute Value Through a Method
        self.odometer_reading = self.odometer_reading + miles


my_new_car = Car('audi', 'a4', 2024)
print(my_new_car.get_descriptive_name())

my_new_car.odometer_reading = 23                                    #modifying an attribute's Value directly
my_new_car.read_odometer()     

my_new_car.update_odometer(29)                                      #Modifying an attribute's Value Through a Method
my_new_car.read_odometer()

my_used_car = Car('subaru', 'outback', 2019)
print("\n")
print(my_used_car.get_descriptive_name())

my_used_car.update_odometer(23_500)
my_used_car.read_odometer()

my_used_car.increment_odometer(10000)                                #incrementing an attribute Value Through a Method
my_used_car.read_odometer()




    
        