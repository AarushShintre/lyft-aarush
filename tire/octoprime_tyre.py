from tire.tire import Tire

class octoprimeTire(Tire):
    def __init__(self, tire_wear):
        self.tire_wear = tire_wear

    def needs_service(self):
        sum = 0
        for i in self.tire_wear:
            sum = i+sum
        if sum >= 3:
            return True
        else:
            return False
