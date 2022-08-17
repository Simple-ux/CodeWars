import sys
sys.path.append("../../")
from CodeWars.Tasks_Solutions.Regex_validate_PIN_code import validate_pin

def test_validate_1():
    assert validate_pin("132452") == True
def test_validate_2():
    assert validate_pin("1232") == True
def test_validate_3():
    assert validate_pin("Ac2132") == False
def test_validate_4():
    assert validate_pin("653") == False
def test_validate_5():
    assert validate_pin("22132") == False
def test_validate_6():
    assert validate_pin("3253.3") == False
def test_validate_7():
    assert validate_pin("2!32") == False