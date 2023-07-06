from Carclass_prog import Car

Broomie = Car("2005 Innova", "Toyota", 0)
Acceleration = 0

while(Acceleration != 5):
    Broomie.accelerate()
    Acceleration = Acceleration + 1
    Broomie_Status_Acceleration = Broomie.get_speed()
    print(f"You accelerated, Broomie's speed is {Broomie_Status_Acceleration} km/h")

    