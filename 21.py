import time 
start  = time.time()
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
    list1 = list1[:-1]
    return [list1,suma(list1)]
    #return count
#print(factors(220))

def ambilicle(x,limit,yes=[],process=[]):
    y = factors(x)[1]
    k = factors(y)[1]
    #print(x,k)
    if x == k and y != x:
        if y not in yes:
            if y < limit:
                yes.append(y)
        if k not in yes:
            if k < limit:
                yes.append(k)
    if y not in process:
        if y < limit:
            process.append(y)

def iterate(limit):
    yes,process = [],[]
    for i in range(1,limit):
        if i in process:
            continue
        else:
            process.append(i)
            ambilicle(i,limit,yes,process)
    #for i in range(limit):
    #    if i in process:
    #        continue
    #    else:
    #        print("values missed:",i)
    #print(sorted(process))
    print(yes)
    return suma(yes)

#print(ambilicle(220))
print(iterate(10000))
end = time.time()
print(end-start)