from Fanclass_prog import Fan

class TestFan():
    def fc_test_run(self):
        self.__Fan_1 = Fan(Fan.FAST, 10, "YELLOW", True)
        self.__Fan_2 = Fan(Fan.MEDIUM, 5, "BLUE", False)
        
        print("""Welcome to Fan prog!
    Let's see the status of your 2 fans!""")
        
        print(" ------- ||| FAN #1 ||| -------")
        print("Status: ", self.__Fan_1.get_status())
        print("Speed: ", self.__Fan_1.get_speed())
        print("Radius: ", self.__Fan_1.get_radius())
        print("Color: ", self.__Fan_1.get_color())
        
        print(" ------- ||| FAN #2 ||| -------")
        print("Status: ", self.__Fan_2.get_status())
        print("Speed: ", self.__Fan_2.get_speed())
        print("Radius: ", self.__Fan_2.get_radius())
        print("Color: ", self.__Fan_2.get_color())


run = TestFan()
run.fc_test_run()