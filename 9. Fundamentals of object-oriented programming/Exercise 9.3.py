# Again, extend the program by adding a new drive method that receives the number of hours as a parameter.
# The method increases the travelled distance by how much the car has travelled in constant speed in the given time.
# Example: The travelled distance of car object is 2000 km.
# The current speed is 60 km/h. Method call car.drive(1.5) increases the travelled distance to 2090 km.

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

    def drive(self, travel_time):
        self.travelled_distance = self.travelled_distance + travel_time * self.current_speed
        print(f"Current travelled distance of the new car after driving {travel_time} h at {self.current_speed:d} km/h is {self.travelled_distance:d} km \n")

car1 = Car("ABC-123", 142)

car1.accerelate(30)
car1.drive(2)
car1.accerelate(70)
car1.drive(2)
car1.accerelate(50)
car1.drive(1)
car1.accerelate(-200)
car1.drive(1)

print(f"New car's properties are: \n Registration number: {car1.registration_number:s}, \n Maximum speed of {car1.max_speed:d} km/h,\n "
      f"Current speed of {car1.current_speed:d} km/h, \n Travelled distance of {car1.travelled_distance:d} km.")