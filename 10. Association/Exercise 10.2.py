# Extend the previous program by creating a Building class.
# The initializer parameters for the class are the numbers of the bottom and top floors and the number of elevators in the building.
# When a building is created, the building creates the required number of elevators. The list of elevators is stored as a property of the building.
# Write a method called run_elevator that accepts the number of the elevator and the destination floor as its parameters.
# In the main program, write the statements for creating a new building and running the elevators of the building.

class Building:
    def __init__(self, bottom_floor_number, top_floor_number, elevator_number):
        self.bottom_floor_number = bottom_floor_number
        self.top_floor_number = top_floor_number
        self.elevator_number = elevator_number
        self.elevator_list = []
        for i in range(elevator_number):
            elevator = Elevator(bottom_floor_number, top_floor_number)
            self.elevator_list.append(elevator)
        print(self.elevator_list)

    def run_elevator(self, number_of_elevator, destination_floor):
        called_elevator = self.elevator_list[number_of_elevator - 1]
        return called_elevator.go_to_floor(destination_floor)


class Elevator:
    def __init__(self, bottom_floor, top_floor):
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
        return self.current_floor

    def floor_up(self):
        self.current_floor = self.current_floor + 1
        print(f"You are at {self.current_floor} floor")
        return self.current_floor

    def floor_down(self):
        self.current_floor = self.current_floor - 1
        print(f"You are at {self.current_floor} floor")
        return self.current_floor

building1 = Building(0,10,4)

new_desired_floor = building1.run_elevator(1,8)
print(f"Elevator 1 is at {new_desired_floor} floor")

new_desired_floor = building1.run_elevator(1,2)
print(f"Elevator 1 is at {new_desired_floor} floor")

new_desired_floor = building1.run_elevator(2,11)
print(f"Elevator 2 is at {new_desired_floor} floor")

new_desired_floor = building1.run_elevator(2,6)
print(f"Elevator 2 is at {new_desired_floor} floor")

