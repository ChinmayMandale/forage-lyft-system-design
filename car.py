from abc import ABC, abstractmethod

from battery_package.nubbin_battery import NubbinBattery
from battery_package.spindler_battery import SpindlerBattery
from engine_package.capulet_engine import CapuletEngine
from engine_package.sternman_engine import SternmanEngine
from engine_package.willoughby_engine import WilloughbyEngine


class Car(ABC):
    def __init__(self, engine_name, battery_name, current_date, current_mileage, last_service_date, last_service_mileage, warning_light_is_on):
        if engine_name == 'Capulet':
            engine = CapuletEngine(current_mileage, last_service_mileage)
        elif engine_name == 'Sternman':
            engine = SternmanEngine(warning_light_is_on)
        elif engine_name == 'Willoughby':
            engine = WilloughbyEngine(current_mileage, last_service_mileage)

        if battery_name == 'Spindler':
            battery = SpindlerBattery(current_date, last_service_date)
        elif battery_name == 'Nubbin':
            battery = NubbinBattery(current_date, last_service_date)

        self.engine = engine
        self.battery = battery

    @abstractmethod
    def needs_service(self):
        pass
