import sys
#print(sys.getrecursionlimit())
def fact(n):
    if n == 1:
        return 1
    else:
        return n * fact(n-1)
    
def stri (x):
    string = str(fact(x))   
    sum = 0
    for k in string:
        sum += int(k) 
    return sum
print(stri(100))