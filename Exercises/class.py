class Car:
    def __init__(self, model, year):
       self.model =  model
       self.year = year
       self.speed = 0

    def accelerate(self):
        self.speed += 10
        print(f"{self.model} {self.year} accelerates to {self.speed}")

    def brake(self):
        self.speed -= 10
        if self.speed < 0:
            self.speed = 0
        print(f"{self.model} slows down to {self.speed}")

    def info(self):
        print(f"This is a {self.year} {self.model}.")

car1 = Car('Mercedes c class',2019)
car1.accelerate()
car1.info()

car2 = Car('Mazda Demio', 2020)
car2.info()
car2.brake()
car2.accelerate( 
    
)