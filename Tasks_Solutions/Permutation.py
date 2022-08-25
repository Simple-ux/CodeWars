# In this kata you have to create all permutations of a non empty input string and remove duplicates, if present. 
# This means, you have to shuffle all letters from the input in all possible orders.

# Examples:

# * With input 'a'
# * Your function should return: ['a']
# * With input 'ab'
# * Your function should return ['ab', 'ba']
# * With input 'aabb'
# * Your function should return ['aabb', 'abab', 'abba', 'baab', 'baba', 'bbaa']


from itertools import permutations

def permut(s):
    result = []
    str = ''
    if len(s) == 1:
        return s

    temp = permutations(s, len(s))
    for i in temp:
        str = "".join(i)
        result.append(str)
    return set(result)