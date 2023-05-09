class Elevator:
    def __init__(self, bottom, top, current):
        """Initializes the Elevator instance."""
        self.bottom = 0
        self.top = 0
        self.current = 0
    
    def __str__(self):
        """Prints the current floor"""
        return "Current floor:{}".format(str(self.current))

    def up(self):
        """Makes the elevator go up one floor."""
        if self.current < 10:
            self.current += 1
        else:
            self.current = 10
        
    def down(self):
        """Makes the elevator go down one floor."""
        if self.current <=10 and self.current > 0:
            self.current -= 1
        
    def go_to(self, floor):
        """Makes the elevator go to the specific floor."""
        if floor <= 0:
            self.current = 0
        elif floor > 10:
            self.current = 0
        else:
            self.current = floor
        

elevator = Elevator(-1, 10, 0)

elevator.up() 
elevator.current #should output 1

elevator.down() 
elevator.current #should output 0

elevator.go_to(10) 
elevator.current #should output 10

# Go to the top floor. Try to go up, it should stay. Then go down.
elevator.go_to(10)
elevator.up()
elevator.down()
print(elevator.current) # should be 9
# Go to the bottom floor. Try to go down, it should stay. Then go up.
elevator.go_to(-1)
elevator.down()
elevator.down()
elevator.up()
elevator.up()
print(elevator.current) # should be 1

elevator.go_to(5)
print(elevator)