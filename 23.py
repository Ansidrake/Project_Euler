def suma(x):
    suma = 0
    for k in x:
        suma+=k
    return suma 

def factors(x):
    result = []
    i = 1
    count = 0
    while i*i <= x:
        if x % i == 0:
            result.append(i)
            if x//i != i: 
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



