#Write class named Pet with the attributes: __name, __animal, __age.
class Pet():
    
    #Pet class should have an __init__ method that has various methods.
    def __init__(self, name, animal_type, age):
        self.__name = name
        self.__animal_type = animal_type
        self.__age = age
    
    #Method that assigns value to the __name
    def set_name(self):
        name = str(input("Enter animal name: ")).upper()
        self.__name = name
    
    #Method that assigns value to the __animal_type
    def set__animal_type(self):
        animal = input("Enter animal type: ").upper()
        self.__animal_type = animal
    
    #Method that assigns value to __age
    def set_age(self):
        age = int(input("Enter animal age: "))
        self.__age = age
    
    #Method returns value to __name
    def get_name(self):
        animal_name = f"Your pet's name is {self.__name}"
        print(animal_name)
        return self.__name
    
    #Method returns value to __animal_type
    def get_animal_type(self):
        animal_type = f"Your pet is a {self.__animal_type}"
        print(animal_type)
        return self.__animal_type
    
    #Method returns value to __age
    def get_age(self):
        animal_age = f"Your pet is {self.__age} years old."
        print(animal_age)
        return self.__age
