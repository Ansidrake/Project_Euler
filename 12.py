import time
start = time.time()
# defining factors 
#def factors(n):
#    count = 1
#    for i in range(1,int((n)/2)+1):
#        if n%i == 0:
#            count+=1
#    return count
#print(factors(28))
def factors(x):
    # We will store all factors in `result`
    result = []
    i = 1
    count = 0
    # This will loop from 1 to int(sqrt(x))
    while i*i <= x:
        # Check if i divides x without leaving a remainder
        if x % i == 0:
            count+=1
            #result.append(i)
            # Handle the case explained in the 4th
            if x//i != i: # In Python, // operator performs integer/floored division
                count+=1
                #result.append(x//i)
        i += 1
    # Return the list of factors of x
    #return result
    return count


#finding triangle numbers
def triangle(n):
    sum = 0
    for k in range(1,n+1):
        sum += k
    return sum
#print(triangle(10))

#def find(n=1):
#    card = len(factors(triangle(n)))
#    if card > 500:
#        return triangle(n)
#    else:
#        return find(n+1)
#print(find())

n = 0
card = 0
while card <= 500:
    card = factors(n+1)
    n+=1
print(n)
print(card)
end = time.time()
print(end-start)