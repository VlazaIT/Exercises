# Now we will program a car race. The travelled distance of a new car is initialized as zero.
# At the beginning of the main program, create a list that consists of 10 car objects created using a loop.
# The maximum speed of each new car is a random value between 100 km/h and 200 km/h.
# The registration numbers are created as follows: "ABC-1", "ABC-2" and so on. Now the race begins.
# One per every hour of the race, the following operations are performed:

    # The speed of each car is changed so that the change in speed is a random value between -10 km/h and +15 km/h. This is done using the accerelate method.
    # Each car is made to drive for one hour. This is done with the drive method.

# The race continues until one of the cars has advanced at least 10,000 kilometers.
# Finally, the properties of each car are printed out formatted into a clear table.

import random

class CarRace:
    def __init__(self, registration_number, max_speed, current_speed, travelled_distance=0):
        self.registration_number = registration_number
        self.max_speed = max_speed
        self.current_speed = current_speed
        self.travelled_distance = travelled_distance

    def accerelate(self, speed_change):
        self.current_speed = self.current_speed + speed_change
        if self.current_speed > self.max_speed:
            self.current_speed = self.max_speed


    def drive(self, travel_time):
        self.travelled_distance = self.travelled_distance + travel_time * self.current_speed
        return self.travelled_distance

cars_list = []
reg_number = 1

for i in range(10):
    m_speed = random.randint(100, 200)  # max speed randomized
    c_speed = random.randint(100, 200)  # current speed randomized
    if c_speed > m_speed:
        c_speed = m_speed
    new_car = CarRace(reg_number, m_speed, c_speed)
    cars_list.append(new_car)
    print(f"Registration number: ABC-{reg_number}, max speed is {m_speed} km/h, current speed is {c_speed} km/h ")
    reg_number = reg_number + 1

time = 0
distance = 0
race_finished = False

while not race_finished:
    time = time + 1
    print(f"\nAfter {time} hours:")
    for new_car in cars_list:
        new_car.accerelate(random.randint(-10,15))
        distance = new_car.drive(1)
        print(f"Car ABC-{new_car.registration_number} with max speed of {new_car.max_speed} km/h and current speed of {new_car.current_speed} km/h has driven {new_car.travelled_distance} km")
        if distance >= 10000:
            race_finished = True

print("Race finished!")
