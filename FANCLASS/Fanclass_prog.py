#Design a class named fan to represent a FAN.
class Fan():
    #Create Three Constants (SLOW, MEDIUM, & FAST) with 3 values (1, 2, & 3) to denote the fan speed.
    SLOW = 1
    MEDIUM = 2
    FAST = 3
    #Constructor that creates fan with specified speed, radius, color, and on (default false)
    def __init__(self, speed = SLOW, radius = 5, color = "BLUE", on = False):    
        #Private int data that specifies speed of fan
        self.speed = speed
        # Private bool data field that specifies whether or not the fan is on(Default is False)
        self.status = on
        #Private string data field that specifies fan color
        self.color = color
        #Private bool data that specifies radius
        self.radius = radius
        
    #Accessor(getter) and mutator(seters) on all four data fields
    def get_speed(self):
        return self.speed
    
    def get_status(self):
        return self.status
    
    def get_radius(self):
        return self.radius
    
    def get_color(self):
        return self.color
    
    def set_speed(self, updated_speed):
        self.speed = updated_speed
    
    def set_status(self, updated_status):
        self.status = updated_status
    
    def set_radius(self, updated_status):
        self.get_radius
    
    def set_color(self, updated_color):
        self.get_color