import sys
sys.path.append("../../")
from CodeWars.Tasks_Solutions.Spin_words import spin_words

def test_spin_1():
    assert spin_words("Happy New Year") == "yppaH New Year"

def test_spin_2():

    assert spin_words("The great power is the great responsibility") == "The taerg rewop is the taerg ytilibisnopser"
def test_spin_3():

    assert spin_words("this is uncommon") == "this is nommocnu"