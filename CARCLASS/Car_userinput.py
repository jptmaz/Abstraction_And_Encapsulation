#Create Class for year and model
class car_year_model():
    #Create Method
    def input_year_model(self):
        try:
            year_model = str(input("Enter Year and Model: "))
        except ValueError:
            print("An error has occured, please try again.")
            year_model = str(input("Enter Year and Model: "))
            
        return year_model

#Create Class for year and model
class car_make():
    #Create Method
    def input_make(self):
        try:
            make = str(input("Enter Year and Model: "))
        except ValueError:
            print("An error has occured, please try again.")
            make = str(input("Enter Manufacturer: "))
            
        return make
