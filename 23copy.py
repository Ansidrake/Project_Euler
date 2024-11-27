
'''

plan for solving this problem:

1. get only the abundant numbers from 1 to 28123
   do this by first getting the factors of all the numbers from 1 to 28123
   do the sum of factors for each number
   if the sum of factors is greater than the number then it is an abundant number

2. then just find all the combinations of this number 
   
'''
import numpy as np
import time

# finding the factor of a number 

# def factors2(x):
#     result = np.array([])
#     i = 1
#     while i*i <= x:
#         if x % i == 0:
#             result = np.append(result,[int(i),int(x//i)])
#         i += 1
#     list1 = sorted(set(result))
#     return list1[:-1]


def factors(x):
    result = []
    i = 1
    count = 0
    while i*i <= x:
        if x % i == 0:
            result.extend([i,x//i])
            # if x//i != i: 
            #     result.append(x//i)
        i += 1
    # Return the list of factors of x
    list1 = sorted(set(result))
    return list1[:-1]

# start = time.time()
# print(factors(220))
# end = time.time()
# time_taken = end - start

# start = time.time()
# print(factors2(220))
# end = time.time()
# time_taken2 = end - start

# if time_taken > time_taken2:
#     print("factors2 is faster")
# else:
#     print("factors is faster")

print(factors(4))

abundant = []
for i in range(1,28124):
    if sum(factors(i)) > i:
        abundant.append(i)

print(min(abundant))

# print(abundant,len(abundant))
# make a list of sums of combinations of abundant numbers
result = set()
for k in range(len(abundant)-1):
    for j in range(k, len(abundant)):
        if abundant[k]+abundant[j] < 28124:
            result.add(abundant[k]+abundant[j])

sum = 0
for i in range(1,28124):
    if i not in result:
        sum += i
print(sum)

