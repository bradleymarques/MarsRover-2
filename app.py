import rover
import inputhandler
import datetime

def log(msg):
    d=datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    print(f"[{d}]: {msg}")
    
def get_grid():
    while True:
        res = inputhandler.validate_grid(input("Enter mars sector coordinates:"))
        if "Please" not in res:
            return res
        else:
            log(res)
    

def get_position(grid):
    while True:
        start = inputhandler.validate_start(input("Enter starting position and direction:"))
        if start[1][0] > grid[1][0] or start[1][1] > grid[1][1]:
            log("Please enter valid starting position and direction")
        else:
            return start

def commands(MarsRover):
    while True:
        input_commands = inputhandler.validate_command(input("Enter command:"))
        print(input_commands)
        for i in input_commands[1]:
            if i == "M":
                log(MarsRover.move())
            if i == "L":
                log(MarsRover.rotate_left())
            if i == "R":
                log(MarsRover.rotate_right())

def main():
    grid = get_grid()
    log(grid)
    
    start = get_position(grid)
    log(start[0])
    
    commands(rover.Rover(start[1][0],start[1][1],grid[1][0],grid[1][1],start[1][3]))
    
main()