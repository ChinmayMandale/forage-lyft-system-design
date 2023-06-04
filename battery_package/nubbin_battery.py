from battery_package.battery import Battery

class NubbinBattery(Battery):
    def __init__(self, last_service_date, current_date):
        self.last_service_date = last_service_date
        self.current_date = current_date

    def needs_service(self):
        diff = self.current_date.year - self.last_service_date.year
        return diff >= 4