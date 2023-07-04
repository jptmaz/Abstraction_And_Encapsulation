from Fanclass_prog import Fan

class Test_Fan:
    def FC_Test_Run(self):
        self.fan_1 = Fan(Fan.FAST, 10, "YELLOW", "TRUE")
        self.fan_2 = Fan(Fan.MEDIUM, 5, "BLUE", "FALSE")
        
    def Test_Run_Stat(self):
        print(''' WELCOME TO FAN PROG!
              Let's check the status of your two fans.
              ''')
        
        print(" ------- ||| FAN #1 ||| -------")
        print("Status: ", self.fan_1.get_status())
        print("Speed: ", self.fan_1.get_speed())
        print("Radius: ", self.fan_1.get_radius())
        print("Color: ", self.fan_1.get_color())
        
        print(" ------- ||| FAN #2 ||| -------")
        print("Status: ", self.fan_2.get_status())
        print("Speed: ", self.fan_2.get_speed())
        print("Radius: ", self.fan_2.get_radius())
        print("Color: ", self.fan_2.get_color())
        

run = Test_Fan
run.Test_Run_Stat()