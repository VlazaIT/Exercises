# Extend the previosly written Car class by adding two subclasses: ElectricCar and GasolineCar.
# Electric cars have the capacity of the battery in kilowatt-hours as their property.
# Gasoline cars have the volume of the tank in liters as their property.
# Write initializers for the subclasses.
# For example, the initializer of electric cars receives the registration number, maximum speed and battery capacity as its parameter.
# It calls the initializer of the base class to set the first two properties and then sets its capacity.
# Write a main program where you create one electric car (ABC-15, 180 km/h, 52.5 kWh) and one gasoline car (ACD-123, 165 km/h, 32.3 l).
# Select speeds for both cars, make them drive for three hours and print out the values of their kilometer counters.

import random

class Car:
    def __init__(self, registration_number, max_speed):
        self.registration_number = registration_number
        self.max_speed = max_speed

    def drive(self):
        for i in range(3):
            selected_speed = random.randint(100, 200)
            if selected_speed > self.max_speed:
                selected_speed = self.max_speed
            travelled_distance = selected_speed * 3
            return travelled_distance

class ElectricCar(Car):
    def __init__(self, registration_number, max_speed, battery_capacity):
        super().__init__(registration_number, max_speed)
        self.battery_capacity = battery_capacity

class GasolineCar(Car):
    def __init__(self, registration_number, max_speed, tank_volume):
        super().__init__(registration_number, max_speed)
        self.tank_volume = tank_volume


electric_car = ElectricCar("ABC-15", 180, 52.5)
electric_car.drive()
print(f"Electric car results:\n Registration number: {electric_car.registration_number}\n Maximum speed: {electric_car.max_speed} km/h\n Travelled distance (after 3 hours): {electric_car.drive()} km\n")
gasoline_car = GasolineCar("CD-123", 165, 32.3)
gasoline_car.drive()
print(f"Gasoline car results:\n Registration number: {gasoline_car.registration_number}\n Maximum speed: {gasoline_car.max_speed} km/h\n Travelled distance (after 3 hours): {gasoline_car.drive()} km")



