import inputhandler
import rover
import random

def test_validate_grid():
    assert "successfully" in inputhandler.validate_grid(str(random.randint(11,99)))[0]
    assert inputhandler.validate_grid(str(random.randint(100,100)))=="Please enter an integer between 11 and 99." 
    assert inputhandler.validate_grid(str(random.randint(0,0)))=="Please enter an integer between 11 and 99." 
    assert inputhandler.validate_grid("-150")=="Please enter an integer between 11 and 99."
    assert inputhandler.validate_grid("115000900900900.00")=="Please enter an integer between 11 and 99."
    assert inputhandler.validate_grid("1.1")=="Please enter an integer between 11 and 99."
    assert inputhandler.validate_grid("%")=="Please enter an integer between 11 and 99."
    assert inputhandler.validate_grid("QQNN")=="Please enter an integer between 11 and 99."
    
def test_validate_start():
    assert "successfully" in inputhandler.validate_start("12 E")[0]
    assert "successfully" not in inputhandler.validate_start("100 E")[0]
    assert "successfully" not in inputhandler.validate_start("10 E")[0]
    assert "successfully" not in inputhandler.validate_start("12 Q")[0]
    assert "successfully" not in inputhandler.validate_start("BEQ")[0]
    assert "successfully" not in inputhandler.validate_start("99")[0]
    assert "successfully" not in inputhandler.validate_start("-50")[0]

def test_validate_command():
    assert "successfully" in inputhandler.validate_command("M")[0]
    assert "successfully" in inputhandler.validate_command("R")[0]
    assert "successfully" in inputhandler.validate_command("L")[0]
    assert "successfully" not in inputhandler.validate_command("Q")[0]
    assert "successfully" not in inputhandler.validate_command("5")[0]
    assert "successfully" not in inputhandler.validate_command("%$")[0]

