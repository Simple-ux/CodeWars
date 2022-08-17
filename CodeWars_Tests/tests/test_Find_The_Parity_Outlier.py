import sys
sys.path.append("../../")
from CodeWars.Tasks_Solutions.Find_The_Parity_Outlier import find_outlier

def test_find_parity_1():
    assert find_outlier([2, 4, 6, 8, 10, 3]) == 3

def test_find_parity_2():
    assert find_outlier([2, 4, 0, 100, 4, 11, 2602, 36]) == 11

def test_find_parity_3():
    assert find_outlier([160, 3, 1719, 19, 11, 13, -21]) == 160