# This exercise continues the previous car race exercise from the last exercise set.
# Write a Race class that has the following properties: name, distance in kilometers and a list of cars participating in the race.
# The class has an initializer that receives the name, kilometers, and car list as parameters and sets their values to the corresponding properties in the class.
# The class has the following methods:

    #hour_passes, which performs the operations done once per hour in the original exercise: generates a random change of speed for each car and calls their drive method.
    #print_status, which prints out the current information of each car as a clear, formatted table.
    #race_finished, which returns True if any of the cars has reached the finish line, meaning that they have driven the entire distance of the race.

# Write a main program that creates an 8000-kilometer race called Grand Demolition Derby.
# The new race is given a list of ten cars similarly to the earlier exercise.
# The main program simulates the progressing of the race by calling the hour_passes in a loop, after which it uses the race_finished method to check if the race has finished.
# The current status is printed out using the print_status method every ten hours and then once more at the end of the race.


import random

class Race:
    def __init__(self, name, distance, list_of_cars):
        self.name = name
        self.distance = distance
        self.list_of_cars = list_of_cars

    def hour_passes(self):
        for new_car in self.list_of_cars:
            speed_change = random.randint(-10, 15)
            new_car.drive(speed_change)

    def print_status(self):
        for new_car in self.list_of_cars:
            new_car.car_info()

    def race_finished(self):
        race_over = False
        for new_car in self.list_of_cars:
            distance = new_car.travelled_distance_info()
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
        print(f"ABC-{self.registration_number}, max speed: {self.max_speed} km/h, current speed: {self.current_speed} km/h, travelled distance: {self.travelled_distance} km")

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

race1 = Race("Grand Demolition Derby", 8000, cars_list)

print(f"Information about cars participating in {race1.name} race:\n")

for i in range(10):
    m_speed = random.randint(100, 200)  # max speed randomized
    c_speed = random.randint(100, 200)  # current speed randomized
    if c_speed > m_speed:
        c_speed = m_speed
    new_car = Car(reg_number, m_speed, c_speed)
    cars_list.append(new_car)
    print(f"Registration number: ABC-{reg_number}, max speed: {m_speed} km/h, current speed: {c_speed} km/h")
    reg_number = reg_number + 1

status = False
time = 1
while not status:
    race1.hour_passes()
    status = race1.race_finished()
    if time % 10 == 0:
        print(f"\nResults after {time} hours of the race:\n")
        race1.print_status()
    time = time + 1

print(f"\n{race1.name} is over! \nThe results are as follows:\n")
race1.print_status()