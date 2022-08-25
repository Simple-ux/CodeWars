import sys
sys.path.append("../../")

from CodeWars.Tasks_Solutions.Permutation import permut 

def test_1():
    assert permut("a") == ['a']

def test_2():
    assert permut("ab") == ['ab', 'ba']

def test_3():
    assert permut("aabb") == ['aabb', 'abab', 'abba', 'baab', 'baba', 'bbaa']

