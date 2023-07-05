#Write a class named Car with the attributes year_model, make, and speed.
class Car():
    #It should have an __init__ method that  accepts the car's year model and make as arguments.
    def __init__(self, year_model, make):
        self.__year_model = year_model
        self.__make = make
        self.__speed = 0
        
    def show_car_stat(self):
        car_status = f"You car is a {self.__year_model} with a make of {self.__make} and is running at a speed of {self.__speed}"
        print(car_status)
        
        
    #The class should have the methods accelerate, break, and get speed.
    def accelerate(self):
        self.__speed = +=5
        return self.__speed
    
    def brake(self):
        self.speed = -=5
        return self.__speed
    
    def get_speed(self):
        speed_status = f"Your car, {self.__year_model} is going at a speed of {self.__speed}"
        print(speed_status)
