import sys
sys.path.append("../../")

from CodeWars.Tasks_Solutions.Strip_Comments import strip_comments

def test_1():
    assert strip_comments('apples, pears # and bananas\ngrapes\nbananas !apples', ['#', '!']) == 'apples, pears\ngrapes\nbananas'

def test_2():
    assert strip_comments('a #b\nc\nd $e f g', ['#', '$']) == 'a\nc\nd'

def test_3():
    assert strip_comments('Jonny B $ Good\ntrue\n water$mellon\n', ['#', '$']) == "Jonny B\ntrue\n water\n"

def test_3():
    assert strip_comments('\t\n\navocados apples watermelons', ['.', '!', '-', ',', '=', '?', '#', "'", '@']) == "\n\navocados apples watermelons"