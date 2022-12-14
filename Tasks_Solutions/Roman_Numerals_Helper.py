# Create a RomanNumerals class that can convert a roman numeral to and from an integer value. 
# It should follow the API demonstrated in the examples below. Multiple roman numeral values will be tested for each helper method.

# Modern Roman numerals are written by expressing each digit separately starting with the left most digit and skipping 
# any digit with a value of zero. 
# In Roman numerals 1990 is rendered: 1000=M, 900=CM, 90=XC; resulting in MCMXC. 2008 is written as 2000=MM, 8=VIII; or MMVIII. 
# 1666 uses each Roman symbol in descending order: MDCLXVI.

# Input range : 1 <= n < 4000

# In this kata 4 should be represented as IV, NOT as IIII (the "watchmaker's four").

# SOLUTION:
romanian = {
'M' :	1000,
'CM' : 900,
'D' :	500,
'CD' : 400,
'C' :	100,
'XC' : 90,
'L' :	50,
'XL' : 40,
'X' :	10,
'IX' : 9,
'V' :	5,
'IV' :	4,
'I' :   1,
}

class RomanNumerals:
    def to_roman(val):
        result = ''
        while val > 0:
            for num in romanian:
                if val - romanian[num] > 0:
                    val -= romanian[num]
                    result += num
                    break

                elif val - romanian[num] == 0:
                    return(result + num)   

            

    def from_roman(roman_num):
        for i in range(4000):
            if RomanNumerals.to_roman(i) == roman_num:
                return i


print(RomanNumerals.to_roman(399))
print(RomanNumerals.from_roman('CCCXCIX'))
