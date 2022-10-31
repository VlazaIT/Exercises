import random

class Race:
    def __init__(self, name, distance, list_of_cars):
        self.name = name
        self.distance = distance
        self.list_of_cars = list_of_cars

    def hour_passes(self):
        for auto in self.list_of_cars:
            speed_change = random.randint(-10, 15)
            auto.drive(speed_change)

    def print_status(self):
        for auto in self.list_of_cars:
            auto.car_info()

    def race_finished(self):
        race_over = False
        for automobile in self.list_of_cars:
            distance = automobile.travelled_distance_info()
            if distance >= self.distance:
                race_over = True
        return race_over

class Car:
    def __init__(self, registration_number, max_speed, current_speed, travelled_distance=0):
        self.registration_number = registration_number
        self.max_speed = max_speed
        self.current_speed = current_speed
        self.travelled_distance = travelled_distance

    def car_info(self):
        print(f"ABD-{self.registration_number}, current speed: {self.current_speed} km/h, travelled distance: {self.travelled_distance} km")

    def travelled_distance_info(self):
        return self.travelled_distance


    def drive(self, speed_change):
        self.current_speed = self.current_speed + speed_change
        if self.current_speed > self.max_speed:
            self.current_speed = self.max_speed
        self.travelled_distance = self.travelled_distance + self.current_speed
        return self.travelled_distance, self.current_speed

cars_list = []
reg_number = 1

for i in range(10):
    m_speed = random.randint(100, 200)  # max speed randomized
    c_speed = random.randint(100, 200)  # current speed randomized
    if c_speed > m_speed:
        c_speed = m_speed
    new_car = Car(reg_number, m_speed, c_speed)
    cars_list.append(new_car)
    print(f"Registration number: ABC-{reg_number}, max speed is {m_speed} km/h, current speed is {c_speed} km/h ")
    reg_number = reg_number + 1

race1 = Race("Grand Demolition Derby", 8000, cars_list)

status = False
time = 1
while not status:
    race1.hour_passes()
    status = race1.race_finished()
    if time % 10 == 0:
        print(f"\n{time} hours into the race:")
        race1.print_status()
    time = time + 1

print(f"\n{race1.name} has ended! The result is:\n")
race1.print_status()