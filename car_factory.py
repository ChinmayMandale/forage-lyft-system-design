from battery_package.nubbin_battery import NubbinBattery
from battery_package.spindler_battery import SpindlerBattery
from car import Car
from engine_package.capulet_engine import CapuletEngine
from engine_package.sternman_engine import SternmanEngine
from engine_package.willoughby_engine import WilloughbyEngine
from tire_package.carrigan_tire import CarriganTire
from tire_package.octoprime_tire import OctoprimeTire


class CarFactory:
    @staticmethod
    def create_calliope(current_date, last_service_date, current_mileage, last_service_mileage, tire_array):
        engine = CapuletEngine(current_mileage, last_service_mileage)
        battery = SpindlerBattery(current_date, last_service_date)
        tire = CarriganTire(tire_array)
        return Car(engine, battery, tire)

    @staticmethod
    def create_glissade(current_date, last_service_date, current_mileage, last_service_mileage, tire_array):
        engine = WilloughbyEngine(current_mileage, last_service_mileage)
        battery = SpindlerBattery(current_date, last_service_date)
        tire = OctoprimeTire(tire_array)
        return Car(engine, battery, tire)

    @staticmethod
    def create_palindrome(current_date, last_service_date, warning_light_is_on, tire_array):
        engine = SternmanEngine(warning_light_is_on)
        battery = SpindlerBattery(current_date, last_service_date)
        tire = OctoprimeTire(tire_array)
        return Car(engine, battery, tire)

    @staticmethod
    def create_rorschach(current_date, last_service_date, current_mileage, last_service_mileage, tire_array):
        engine = WilloughbyEngine(current_mileage, last_service_mileage)
        battery = NubbinBattery(current_date, last_service_date)
        tire = CarriganTire(tire_array)
        return Car(engine, battery, tire)

    @staticmethod
    def create_thovex(current_date, last_service_date, current_mileage, last_service_mileage, tire_array):
        engine = CapuletEngine(current_mileage, last_service_mileage)
        battery = NubbinBattery(current_date, last_service_date)
        tire = OctoprimeTire(tire_array)
        return Car(engine, battery, tire)

