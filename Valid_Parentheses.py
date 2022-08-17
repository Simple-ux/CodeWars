# Write a function that takes a string of parentheses, and determines if the order of the parentheses is valid. 
# The function should return true if the string is valid, and false if it's invalid.

# Examples
# "()"              =>  true
# ")(()))"          =>  false
# "("               =>  false
# "(())((()())())"  =>  true

def valid_parentheses(string):
    arr = ""
    for i in string:
        if (i == ")"):
            arr += i + ","
        elif (i == "("):
            arr += i
    try:  
        if exec(arr) == None:
            return True
    except:
        return False

# Tests
assert valid_parentheses("hi(ds))(") == False
assert valid_parentheses("()(()())") == True
assert valid_parentheses("9(()(9)))()(") == False
assert valid_parentheses(")") == False
assert valid_parentheses("(") == False


