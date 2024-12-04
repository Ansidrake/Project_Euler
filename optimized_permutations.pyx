import math
from tqdm import tqdm
import time
import cython

@cython.boundscheck(False)
@cython.wraparound(False)
def len_of_permutations(list1, digit_counts):
    """
    Calculate number of unique permutations excluding those starting with 0.
    Optimized version with direct integer calculations.
    """
    cdef int length = len(list1)
    cdef int total_perms = math.factorial(length)
    cdef int zero_perms = 0
    
    # Precompute repeated digit divisors
    for count in digit_counts.values():
        total_perms //= math.factorial(count)
    
    # Calculate leading zero permutations
    if 0 in digit_counts:
        zero_perms = math.factorial(length - 1) // math.factorial(digit_counts[0])
    
    return sum(range(total_perms - zero_perms))

@cython.boundscheck(False)
@cython.wraparound(False)
def dict_to_list(dict1):
    """Convert dictionary to list of digits considering count."""
    list1 = []
    for digit, count in dict1.items():
        list1.extend([digit] * count)
    return list1

def generate_digit_distributions(total_digits: int):
    """
    Optimized digit distribution generation using itertools.
    """
    from itertools import combinations_with_replacement
    
    distributions = []
    for combo in combinations_with_replacement(range(10), total_digits):
        dist = {}
        for digit in combo:
            dist[digit] = dist.get(digit, 0) + 1
        distributions.append(dist)
    
    return distributions

def main(n: int):
    cdef long last = 1
    for i in range(2,n + 1):
        start = time.time()
        dist = generate_digit_distributions(i)
        end = time.time()
        print(f"Distribution generation for {i}: {end - start:.4f}s")
        
        start = time.time()
        sum1 = sum(
            len_of_permutations(dict_to_list(d), d) 
            for d in tqdm(dist, desc=f"Processing {i}-digit distributions")
        )
        end = time.time()
        
        print(f"Time taken for {i} is {end - start:.4f}s")
        print(f"Number of permutations for {i} is {sum1}")
        print(sum1/n)
        print(sum1/len(dist))
        print(sum1/last)
        print(len(dist))
        last = sum1
