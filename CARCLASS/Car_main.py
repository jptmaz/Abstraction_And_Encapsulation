from Car_userinput import car_year_model
from Car_userinput import car_make
from Carclass_prog import Car

class UserInput_Prog(car_year_model, car_make):
    def input_year_model(self):
        return super().input_year_model()
    
    def input_make(self):
        return super().input_make()

class Car_prog(Car):
    def __init__(self, year_model, make, speed):
        super().__init__(year_model, make, speed)
    def accelerate(self):
        return super().accelerate()
    def brake(self):
        return super().brake()
    def get_speed(self):
        return super().get_speed()


