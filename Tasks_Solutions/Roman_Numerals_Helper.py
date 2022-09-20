romanian = {
    'M' : '1000',
    'D' : '500',
    'C' : '100',
    'L' : '50',
    'X' : '10',
    'V' : '5',
    'I' : '1'
            }

def to_roman(val):
    result = ''
    i = val
    n = ''
    while i > 0:
        for num in romanian:
            if val - int(romanian[num]) > 0: 
                val -= int(romanian[num])
                result += num
                break

            elif val - int(romanian[num]) == 0:
                return(result + num)   

            else:
                n = num
                continue
            
print(to_roman(90))
