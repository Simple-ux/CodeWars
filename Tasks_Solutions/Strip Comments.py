# Complete the solution so that it strips all text that follows any of a set of comment markers passed in. 
# Any whitespace at the end of the line should also be stripped out.
# Given an input string of:

#       apples, pears # and bananas
#       grapes
#       bananas !apples
#       The output expected would be:

# The output expected would be:

#       apples, pears
#       grapes
#       bananas

# Solution
import string

def strip_comments(strng, markers):
    strng = strng.split("\n")
    result = []

    for i in strng:
        for marker in markers:
            i = i.split(marker).pop(0).rstrip(" ")
            if markers[-1] == marker:
                result.append(i)
    return "\n".join(result)
