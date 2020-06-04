import math

class Rocket():
    def __init__(self, x=0, y=0):
        self.x = x
        self.y = y
    
    def get_distance(self, other_rocket):
        distance = math.sqrt((self.x-other_rocket.x)**2+(self.y-other_rocket.y)**2)
        return distance