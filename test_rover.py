import rover

def create_rover():
    return rover.Rover("8","8","1","2","E")

def create_rover_negative():
    return rover.Rover("-8","-8","-1","-2","S")

def create_rover_bad_direction():
    return rover.Rover("-8","-8","-1","-2","F")

def test_toofar():
    MarsRover = create_rover()
    assert "failed" in MarsRover.too_far()
    
def test_move():
    MarsRover = create_rover()
    assert "success" in MarsRover.move()

    MarsRover = create_rover_negative()
    assert "success" in MarsRover.move()

    MarsRover = create_rover_bad_direction()
    assert "invalid" in MarsRover.move()

def test_rotate_left():
    MarsRover = create_rover()
    assert "changed" in MarsRover.rotate_left()

    MarsRover = create_rover_negative()
    assert "changed" in MarsRover.rotate_left()

    MarsRover = create_rover_bad_direction()
    assert "invalid" in MarsRover.rotate_left()

def test_rotate_right():
    MarsRover = create_rover()
    assert "changed" in MarsRover.rotate_right()

    MarsRover = create_rover_negative()
    assert "changed" in MarsRover.rotate_right()

    MarsRover = create_rover_bad_direction()
    assert "invalid" in MarsRover.rotate_right()
