from car import Car

class CarFactory:

    def create_calliope(self, current_date, last_service_date, current_mileage, last_service_mileage, warning_light_is_on):
        engine_name = 'Capulet'
        battery_name = 'Spindler'
        return Car(engine_name, battery_name, current_date, current_mileage, last_service_date, last_service_mileage, warning_light_is_on)

    def create_glissade(self, current_date, last_service_date, current_mileage, last_service_mileage, warning_light_is_on):
        engine_name = 'Willoughby'
        battery_name = 'Spindler'
        return Car(engine_name, battery_name, current_date, current_mileage, last_service_date, last_service_mileage,
                   warning_light_is_on)

    def create_palindrome(self, current_date, last_service_date, current_mileage, last_service_mileage, warning_light_is_on):
        engine_name = 'Sternman'
        battery_name = 'Spindler'
        return Car(engine_name, battery_name, current_date, current_mileage, last_service_date, last_service_mileage,
                   warning_light_is_on)

    def create_rorschach(self, current_date, last_service_date, current_mileage, last_service_mileage, warning_light_is_on):
        engine_name = 'Willoughby'
        battery_name = 'Nubbin'
        return Car(engine_name, battery_name, current_date, current_mileage, last_service_date, last_service_mileage,
                   warning_light_is_on)

    def create_thovex(self, current_date, last_service_date, current_mileage, last_service_mileage, warning_light_is_on):
        engine_name = 'Capulet'
        battery_name = 'Nubbin'
        return Car(engine_name, battery_name, current_date, current_mileage, last_service_date, last_service_mileage,
                   warning_light_is_on)

