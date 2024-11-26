def suma(x):
    suma = 0
    for k in x:
        suma+=k
    return suma 

def factors(x):
    # We will store all factors in `result`
    result = []
    i = 1
    count = 0
    # This will loop from 1 to int(sqrt(x))
    while i*i <= x:
        # Check if i divides x without leaving a remainder
        if x % i == 0:
            #count+=1
            result.append(i)
            # Handle the case explained in the 4th
            if x//i != i: # In Python, // operator performs integer/floored division
                #count+=1
                result.append(x//i)
        i += 1
    # Return the list of factors of x
    list1 = sorted(result)
    return list1[:-1]

def is_perfect(x):
    k = suma((factors(x)))
    if k <= x :
        return False
    else:
        return True

list_abundant = []
for i in range(1,28123):
    if is_perfect(i):
        list_abundant.append(i)

#print(list_abundant)
result = []
for k in list_abundant:
    for j in list_abundant:
        if k+j < 28124 and k+j not in result:
            result.append(k+j)

sum = 0
for i in range(1,28123):
    if i not in result:
        sum += i
print(sum)



