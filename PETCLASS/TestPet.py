from Petclass_prog import Pet

def main():
    pc_prog = Pet("","", 0)
    
    while(True):
        print("Welcome to the Vettie! Your Pet Program!")
        print("Do you want to use Vettie?")
        Vettie_command = input(str("= ")).upper()
        if Vettie_command == "YES":
            pet_name = pc_prog.set_name()
            print(pc_prog.get_name())
            pet_type = pc_prog.set__animal_type()
            print(pc_prog.get_animal_type())
            pet_age = pc_prog.set_age()
            print(pc_prog.get_age())
            Vettie_pet = f"Your pet, {pc_prog.get_name}, is a/an {pc_prog.get_animal_type}, and is a/an {pc_prog.get_age}"
            print(Vettie_pet)
        elif Vettie_command == "NO":
            break
        else:
            print("I don't understand. Please try again.")
            True

if __name__ == "__main__":
    main()