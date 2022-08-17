import sys
sys.path.append('../../')
from CodeWars.Tasks_Solutions.pig_it import pig_it

def test_pig_it_1():
    assert pig_it('O tempora o mores !') == "Oay emporatay oay oresmay !"

def test_pig_it_2():
    assert pig_it('School is cool') == "choolSay siay oolcay"
    
def test_pig_it_3():
    assert pig_it('Over the rainbow bird is fly') == "verOay hetay ainbowray irdbay siay lyfay"



