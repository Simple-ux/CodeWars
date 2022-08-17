# ATM machines allow 4 or 6 digit PIN codes and PIN codes cannot contain anything but exactly 4 digits or exactly 6 digits.
# If the function is passed a valid PIN string, return true, else return false.
# Examples (Input --> Output)
# "1234"   -->  true
# "12345"  -->  false
# "a234"   -->  false

# Solution:

import re
def validate_pin(pin):
    if (re.findall(r"\D", pin) == []) and ((len(pin) == 4) or (len(pin) == 6)): 
        return True
    else :
        return False

# Tests

assert validate_pin("132452") == True
assert validate_pin("1232") == True
assert validate_pin("Ac2132") == False
assert validate_pin("653") == False
assert validate_pin("22132") == False
assert validate_pin("3253.3") == False
assert validate_pin("2!32") == False