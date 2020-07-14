#Uses python3

import sys

def largest_number(a):
    #write your code here
    res = ""
   
    while len(a) != 0:
        Max = ""
        for x in a:
            if isGreaterOrEqual(x,Max):
                Max = x
        res += Max
        if Max in a:
            a.remove(Max)
    return res

def isGreaterOrEqual(a,b):
    if len(b)==0:
        return True
    if int(a+b) >= int(b+a):
        return True
    else:
        return False
    
if __name__ == '__main__':
    input = sys.stdin.read()
    data = input.split()
    a = data[1:]
    print(largest_number(a))
    
