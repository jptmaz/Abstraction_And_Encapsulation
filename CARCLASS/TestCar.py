from Car_main import UserInput_Prog
from Car_main import Car_prog

def main():
    ui = UserInput_Prog
    CarProg = Car_prog
    
    print("Welcome to CarProg! Before we begin, tell me about your car Broomie!")
    year_model = ui.input_year_model()
    make = ui.input_make()


if __name__ == "__main__":
    main()