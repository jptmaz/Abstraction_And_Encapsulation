from Carclass_prog import Car

Broomie = Car("2005 Innova", "Toyota", 0)
Acceleration = 0

while(Acceleration != 5):
    Broomie.accelerate()
    Acceleration = Acceleration + 1
    Broomie_Status_Acceleration = Broomie.get_speed()
    print(f"You accelerated, Broomie's speed is {Broomie_Status_Acceleration} km/h")

Brake = Acceleration
print(f"Brake is = {Brake}")

while(Brake != 0):
    Broomie.brake()
    Brake = Brake - 1
    Broomie_Status_Brake = Broomie.get_speed()
    print(f"You used the brakes, you're slowing down to {Broomie_Status_Brake} km/h.")