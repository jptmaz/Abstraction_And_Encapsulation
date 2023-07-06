#Write a class named Car
#The class must have the attributes __year_model, __make, and __speed
#The class should have an _ _init_ _ method that accepts the car’s year model and make as arguments. These values should be assigned to the object’s _ _year_model and _ _make data attributes. It should also assign 0 to the _ _speed data attribute.
class Car():
    def __init__(self, year_model, make, speed):
        self.__year_model = year_model
        self.__make = make
        self.__speed = 0
        
    #The class should have the methods, accelerate, brake, and get_speed.
    def accelerate(self):
        while self.__speed != 5:
            self.__speed = self.__speed + 1
    
    def brake(self):
           while self.__speed != 0:
            self.__speed = self.__speed - 1
        
    def get_speed(self):
        return self.__speed