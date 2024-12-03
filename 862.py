'''
Larger Digit Permutation
Problem 862

For a positive integer  n , define  T(n)  to be the number of strictly larger integers that can be formed by permuting the digits of  n .

Leading zeros are not allowed, and so for  n = 2302 , the total list of permutations would be:
2023, 2032, 2203, 2230, 2302, 2320, 3022, 3202, 3220

Giving  T(2302) = 4 .

Further define  S(k)  to be the sum of  T(n)  for all  k -digit numbers  n . You are given  S(3) = 1701 .

Find  S(12) .

'''


'''
Thought process 

brute for the shit out of it

'''
import numpy as np

from itertools import permutations

def get_permutations(n):
    list1 = [int(i) for i in str(n)]
    list1 = list(permutations(list1))
    filtered_list = [t for t in list1 if t[0] != 0]
    ls = [int(''.join(map(str,i))) for i in filtered_list]
    return list(set(ls)) # remove duplicates and return ls

# print(get_permutations(2302))


def T(n):
    return sum(1 for num in get_permutations(n) if num > n)
# import time 
# start = time.time()
# print(T(23028407))
# end = time.time()
# print(end-start)

# below code gives a memmory error
# import time 
# start = time.time()
# print(T(149164916294))
# end = time.time()
# print(end-start)


# def S(k):
#     return sum(T(n) for n in range(10**(k-1),10**k))

# print(S(12))





'''
smart easy solution 

make lists of all the possible numbers and if the list exists in a particular list gahter those and thus compare them 



'''



def find_all_permutations(n):
    digit_list = []
    for k in range(10**(n-1),10**n):
        # print(k)
        digits = [int(i) for i in str(k)]
        # print(digits)
        digit_list.append(digits)
    # digits = np.array(digit_list)
    return digit_list
# print(find_all_permutations(4))
# print(i for i in range(10**(4-1),10**4)])
def _list_to_int(list1):
    return int(''.join(map(str,list1)))

def _int_to_list(n):
    return [int(i) for i in str(n)]

# def T(n):
#     digits = find_all_permutations(n)
#     for 

def T(n):
    digits = find_all_permutations(len(str(n)))
    similar = []
    n_list = _int_to_list(n)
    # print(digits)
    for k in digits:
        # print(n_list,k)
        if sorted(n_list) == sorted(k):
            if _list_to_int(k) > n:
                # print(_list_to_int(k),n)
                similar.append(_list_to_int(k))
    return len(similar)

# print(find_all_permutations(4))
# import time
# start = time.time()
# print(T(23028407))
# end = time.time()
# print(end-start)






# geniuos solution by me 
'''


create dictionaries with count of each digit and we start with the highest digit 
ie 999999999...
and represent it as {1:0,2:0,3:0,4:0,5:0,6:0,7:0,8:0,9:12}
for n = 12
and basically generate all the possible bins of 12 digits
ie {1:0,2:0,3:2,4:1,5:2,6:1,7:0,8:2,9:3} and so on

'''
def generate_digit_distributions(total_digits):
    """
    Generate all possible digit distributions for a given number of digits.
    """
    distributions = []
    
    # Helper function to generate distributions recursively
    def backtrack(remaining_digits, current_dist):
        if remaining_digits == 0:
            distributions.append(current_dist.copy())
            return
        
        for digit in range(0, 10):  # Skip 0
            if sum(current_dist.values()) + digit <= total_digits:
                current_dist[digit] = current_dist.get(digit, 0) + 1
                backtrack(remaining_digits - 1, current_dist)
                current_dist[digit] -= 1
                if current_dist[digit] == 0:
                    del current_dist[digit]
    
    backtrack(total_digits, {})
    return distributions


last = 1
# for i in range(1,12):
#     dist = generate_digit_distributions(i)
#     print(len(dist)/last)
#     last = len(dist)
#     print(last)

# output to this was 
'''
2.0
2
3.0
6
4.0
24
5.0
120
6.0
720
7.0
5040
8.0
40320
9.0
362880
10.0
3628800
11.0
39916800
12.0
479001600
13.0
6227020800
'''
from math import factorial
def dict_to_list(dict1):
    """Convert dictionary to list of digits considering count."""
    list1 = []
    for digit, count in dict1.items():
        list1.extend([digit] * count)
    return list1
# print(dict_to_list({0:0,1:0,2:0,7:0,8:0,9:2}))

# def len_of_permutations(list1):
#     permutation = list(permutations(list1))
#     print(permutation)
#     return len(permutation)

def generate_digit_distributions(total_digits):
    distributions = []

    def backtrack(remaining_digits, current_dist, start_digit):
        if remaining_digits == 0:
            distributions.append(current_dist.copy())
            return
        for digit in range(start_digit, 10):  # Digits 0-9
            current_dist[digit] = current_dist.get(digit, 0) + 1
            backtrack(remaining_digits - 1, current_dist, digit)
            current_dist[digit] -= 1
            if current_dist[digit] == 0:
                del current_dist[digit]

    backtrack(total_digits, {}, 0)
    return distributions

def len_of_permutations(list1):
    """
    Calculate number of unique permutations excluding those starting with 0.
    """
    # Precalculate unique permutations
    total_perms = factorial(len(list1))
    
    # Count occurrences of each digit
    digit_counts = {}
    for digit in list1:
        digit_counts[digit] = digit_counts.get(digit, 0) + 1
    
    # Divide total permutations by repeated digit factorials
    for count in digit_counts.values():
        total_perms //= factorial(count)
    
    # Calculate leading zero permutations
    zero_perms = 0
    if 0 in digit_counts and list1[0] == 0:
        # Total permutations if first digit is 0
        zero_perms = factorial(len(list1) - 1)
        zero_digit_counts = {k:v for k,v in digit_counts.items() if k != 0}
        for count in zero_digit_counts.values():
            zero_perms //= factorial(count)
    
    total_perms = total_perms - zero_perms
    
    return sum(i for i in range(total_perms))


# third iteration

# tests
import time
# start = time.time()
# # print(len_of_permutations(dict_to_list({0:0,1:0,2:0,7:0,8:0,9:3})))
# import random
# numbers = [random.randint(0, 9) for _ in range(12)]
# # print(len_of_permutations(dict_to_list({i:numbers.count(i) for i in set(numbers)})))
# # print(len_of_permutations(dict_to_list({0:1,2:2,3:1})))
# end = time.time()
# print((end-start)*6227020800)
# output
'''
(0, 1)
(15, 6)
(36, 9)
'''
from optimized_permutations import len_of_permutations
last = 1

for i in range(12,13):
    start = time.time()
    dist = generate_digit_distributions(i)
    sum1 = 0
    for j in range(len(dist)):
        sum1 += len_of_permutations(dict_to_list(dist[j]))
    # print(sum1/last)
    end = time.time()
    print("Time taken for",i,"is",end-start)
    print("Number of permutations for",i,"is",sum1)
    last = sum1

'''
Time taken for 1 is 4.00543212890625e-05
Number of permutations for 1 is 0
Time taken for 2 is 0.0002779960632324219
Number of permutations for 2 is 36
Time taken for 3 is 0.0007281303405761719
Number of permutations for 3 is 1701
Time taken for 4 is 0.002708911895751953
Number of permutations for 4 is 68418
Time taken for 5 is 0.004664897918701172
Number of permutations for 5 is 2894697
Time taken for 6 is 0.04688310623168945
Number of permutations for 6 is 134537715
Time taken for 7 is 0.2903439998626709
Number of permutations for 7 is 6853222674
Time taken for 8 is 2.191204071044922
Number of permutations for 8 is 377494043598
Time taken for 9 is 21.7866427898407
Number of permutations for 9 is 22176155292300
next is expected to take too longand 12 would be further longer 
'''