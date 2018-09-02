import pexpect

def test_happy_path():
    child = pexpect.spawn ('python app.py')
    child.expect("Enter mars sector coordinates:")
    child.sendline("88")
    child.expect("Enter starting position and direction:")
    child.sendline("12 E")
    child.expect("Enter command:")
    child.sendline("M")
    child.expect("success")
    print(child.before)

def test_sad_path_bad_coordinates():
    child = pexpect.spawn ('python app.py')
    child.expect("Enter mars sector coordinates:")
    child.sendline("Q")
    child.expect("integer between 11 and 99.")    
    assert "Please enter an" in str(child.before)


def test_sad_path_bad_position():
    child = pexpect.spawn ('python app.py')
    child.expect("Enter mars sector coordinates:")
    child.sendline("88")
    child.expect("Enter starting position and direction:")
    child.sendline("EEEEE")
    child.expect("valid starting position and direction")
    assert "Please enter" in str(child.before)

def test_sad_path_invalid_command():
    child = pexpect.spawn ('python app.py')
    child.expect("Enter mars sector coordinates:")
    child.sendline("88")
    child.expect("Enter starting position and direction:")
    child.sendline("12 E")
    child.expect("Enter command:")
    child.sendline("Q")
    child.expect("valid command")
    assert "is not" in str(child.before)



