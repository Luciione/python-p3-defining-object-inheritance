from vehicle import Vehicle

class Car(Vehicle):
    def go(self):
        return "VRRROOOOOOOOOOOOOOOOOOOOOOOM!!!!!"

    def fill_up_tank(self):
        return "filling up!"

    def honk(self):
        return "HONK HONK"

    def drive_fast(self):
        return "Driving so fast"

    def is_motorized(self):
        return True

    def num_wheels(self):
        return self.wheel_number