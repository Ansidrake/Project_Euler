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

print(T(2302))

def S(k):
    return sum(T(n) for n in range(10**(k-1),10**k))

print(S(12))