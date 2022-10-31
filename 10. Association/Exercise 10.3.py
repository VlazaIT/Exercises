# Extend the program again by adding a method fire_alarm that does not receive any parameters and moves all elevators to the bottom floor.
# Continue the main program by causing a fire alarm in your building.

class Building:
    def __init__(self, bottom_floor_number, top_floor_number, elevator_number):
        self.bottom_floor_number = bottom_floor_number
        self.top_floor_number = top_floor_number
        self.elevator_number = elevator_number
        self.elevator_list = []
        for i in range(elevator_number):
            elevator = Elevator(bottom_floor_number, top_floor_number)
            self.elevator_list.append(elevator)

    def run_elevator(self, number_of_elevator, destination_floor):
        called_elevator = self.elevator_list[number_of_elevator - 1]
        return called_elevator.go_to_floor(destination_floor)

    def fire_alarm(self):
        for elevator in range(self.elevator_number):
            print("Fire alarm!")
            self.elevator_list[elevator].go_to_floor(1)

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

building1 = Building(1,10,3)

new_desired_floor = building1.run_elevator(1,8)
print(f"Elevator 1 is at {new_desired_floor} floor")

new_desired_floor = building1.run_elevator(2,6)
print(f"Elevator 2 is at {new_desired_floor} floor")

new_desired_floor = building1.run_elevator(3,11)
print(f"Elevator 3 is at {new_desired_floor} floor")

building1.fire_alarm()