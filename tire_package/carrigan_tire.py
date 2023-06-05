from tire_package.tire import Tire


class CarriganTire(Tire):
    def __init__(self, tire_array):
        self.tire_array = tire_array

    def needs_service(self):
        if any(self.tire_array) >= 0.9:
            return True
