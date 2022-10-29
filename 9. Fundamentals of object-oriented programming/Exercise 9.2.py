# Extend the program by adding an accerelate method into the new class.
# The method should receive the change of speed (km/h) as a parameter.
# If the change is negative, the car reduces speed.
# The method must change the value of the speed property of the object.
# The speed of the car must stay below the set maximum and cannot be less than zero.
# Extend the main program so that the speed of the car is first increased by +30 km/h, then +70 km/h and finally +50 km/h.
# Then print out the current speed of the car.
# Finally, use the emergency brake by forcing a -200 km/h change on the speed and then print out the final speed.
# The travelled distance does not have to be updated yet.

class Car:
    def __init__(self, registration_number, max_speed, current_speed=0, travelled_distance=0):
        self.registration_number = registration_number
        self.max_speed = max_speed
        self.current_speed = current_speed
        self.travelled_distance = travelled_distance

    def accerelate(self, speed_change):
            self.current_speed = self.current_speed + speed_change
            if self.current_speed > self.max_speed:
                self.current_speed = self.max_speed
            elif self.current_speed <= 0:
                self.current_speed = 0
            print(f"Current speed of the new car after accerelating by {speed_change:d} km/h is {self.current_speed:d} km/h")

car1 = Car("ABC-123", 142)

print(f"New car's properties are: \n Registration number: {car1.registration_number:s}, \n Maximum speed of {car1.max_speed:d} km/h,\n "
      f"Current speed of {car1.current_speed:d} km/h, \n Travelled distance of {car1.travelled_distance:d} km. \n")

car1.accerelate(30)
car1.accerelate(70)
car1.accerelate(50)
car1.accerelate(-200)
