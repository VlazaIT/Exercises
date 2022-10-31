# Write an Elevator class that receives the numbers of the bottom and top floors as initializer parameters.
# The elevator has methods go_to_floor, floor_up and floor_down.
# A new elevator is always at the bottom floor.
# If you make elevator h for example the method call h.go_to_floor(5), the method calls either the floor_up or floor_down methods as many times as it needs to get to the fifth floor.
# The methods run the elevator one floor up or down and tell what floor the elevator is after each move.
# Test the class by creating an elevator in the main program, tell it to move to a floor of your choice and then back to the bottom floor.

class Elevator:
    def __init__(self, bottom_floor=0, top_floor=10):
        self.bottom_floor = bottom_floor
        self.top_floor = top_floor
        self.current_floor = bottom_floor

    def go_to_floor(self, chosen_floor):
        print(f"Selected floor: {chosen_floor} and you are now at {self.current_floor} floor")
        if self.current_floor <= chosen_floor:
            if chosen_floor > self.top_floor:
                for i in range(self.top_floor - self.current_floor):
                    self.floor_up()
                self.current_floor = self.top_floor
            else:
                for i in range(chosen_floor - self.current_floor):
                    self.floor_up()
                self.current_floor = chosen_floor
        else:
            if chosen_floor < self.bottom_floor:
                for i in range(self.current_floor - self.bottom_floor):
                    self.floor_down()
                self.current_floor = self.bottom_floor
            else:
                for i in range(self.current_floor - chosen_floor):
                    self.floor_down()
                self.current_floor = chosen_floor

    def floor_up(self):
        self.current_floor = self.current_floor + 1
        print(f"You are at {self.current_floor} floor")

    def floor_down(self):
        self.current_floor = self.current_floor - 1
        print(f"You are at {self.current_floor} floor")


elevator1 = Elevator()
elevator1.go_to_floor(5)
elevator1.go_to_floor(-1)
elevator1.go_to_floor(12)
elevator1.go_to_floor(elevator1.bottom_floor)