import sys
sys.path.append("../../")

from CodeWars.Tasks_Solutions.Valid_Parentheses import valid_parentheses

def test_valid_1():
    assert valid_parentheses("hi(ds))(") == False

def test_valid_2():
    assert valid_parentheses("()(()())") == True

def test_valid_3():
    assert valid_parentheses("9(()(9)))()(") == False

def test_valid_4():
    assert valid_parentheses(")") == False

def test_valid_5():
    assert valid_parentheses("(") == False