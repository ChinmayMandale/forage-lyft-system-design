from battery_package.nubbin_battery import NubbinBattery
from battery_package.spindler_battery import SpindlerBattery
from car import Car
from engine_package.capulet_engine import CapuletEngine
from engine_package.sternman_engine import SternmanEngine
from engine_package.willoughby_engine import WilloughbyEngine


class CarFactory:
    @staticmethod
    def create_calliope(self, current_date, last_service_date, current_mileage, last_service_mileage):
        engine = CapuletEngine(current_mileage, last_service_mileage)
        battery = SpindlerBattery(current_date, last_service_date)
        return Car(engine, battery)

    @staticmethod
    def create_glissade(self, current_date, last_service_date, current_mileage, last_service_mileage):
        engine = WilloughbyEngine(current_mileage, last_service_mileage)
        battery = SpindlerBattery(current_date, last_service_date)
        return Car(engine, battery)

    @staticmethod
    def create_palindrome(self, current_date, last_service_date, warning_light_is_on):
        engine = SternmanEngine(warning_light_is_on)
        battery = SpindlerBattery(current_date, last_service_date)
        return Car(engine, battery)

    @staticmethod
    def create_rorschach(self, current_date, last_service_date, current_mileage, last_service_mileage):
        engine = WilloughbyEngine(current_mileage, last_service_mileage)
        battery = NubbinBattery(current_date, last_service_date)
        return Car(engine, battery)

    @staticmethod
    def create_thovex(self, current_date, last_service_date, current_mileage, last_service_mileage, warning_light_is_on):
        engine = CapuletEngine(current_mileage, last_service_mileage)
        battery = NubbinBattery(current_date, last_service_date)
        return Car(engine, battery)

