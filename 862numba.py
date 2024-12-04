import numpy as np
import numba as nb
import math
import time
from tqdm import tqdm

@nb.njit
def dict_sum(d):
    """
    Manually sum dictionary values for Numba compatibility.
    
    Parameters:
    -----------
    d : dict-like
        Dictionary to sum
    
    Returns:
    --------
    int
        Sum of dictionary values
    """
    total = 0
    for key in range(10):  # Assuming digits 0-9
        total += d.get(key, 0)
    return total

@nb.njit
def factorial_cached(n):
    """Cached factorial calculation for small numbers."""
    factorials = [1, 1, 2, 6, 24, 120, 720, 5040, 40320, 362880]
    return factorials[n] if n < 10 else math.factorial(n)

@nb.njit
def len_of_permutations(list1, digit_counts):
    """
    Calculate number of unique permutations excluding those starting with 0.
    
    Parameters:
    -----------
    list1 : array-like
        List of digits
    digit_counts : dict-like
        Counts of each digit in the list
    
    Returns:
    --------
    int
        Number of unique permutations
    """
    length = len(list1)
    total_perms = factorial_cached(length)
    
    # Divide by factorial of repeated digits
    zero_perms = 0
    for digit in range(10):
        count = digit_counts.get(digit, 0)
        if count > 1:
            total_perms //= factorial_cached(count)
        
        # Calculate leading zero permutations
        if digit == 0 and count > 0:
            zero_perms = factorial_cached(length - 1)
            zero_perms //= factorial_cached(count)
    
    return max(0, total_perms - zero_perms)

@nb.njit
def dict_to_list(digit_counts):
    """
    Convert dictionary to list of digits considering count.
    
    Parameters:
    -----------
    digit_counts : dict-like
        Counts of each digit
    
    Returns:
    --------
    list
        Flattened list of digits
    """
    list1 = []
    for digit in range(10):
        count = digit_counts.get(digit, 0)
        list1.extend([digit] * count)
    return list1

@nb.njit
def generate_digit_distributions(total_digits):
    """
    Generate all possible digit distributions.
    
    Parameters:
    -----------
    total_digits : int
        Total number of digits to distribute
    
    Returns:
    --------
    list
        List of digit distributions
    """
    distributions = []
    
    # Initialize the first distribution
    current_dist = {0: 0}
    
    while True:
        # Check if we've found a valid distribution
        if dict_sum(current_dist) == total_digits:
            distributions.append(current_dist.copy())
        
        # Generate next distribution
        found_next = False
        for digit in range(9, -1, -1):
            if digit in current_dist:
                current_dist[digit] += 1
                if dict_sum(current_dist) > total_digits:
                    current_dist[digit] -= 1
                    del current_dist[digit]
                else:
                    found_next = True
                    break
            elif digit > 0:  # Avoid leading zeros except for initial case
                current_dist[digit] = 1
                found_next = True
                break
        
        # If no more distributions can be generated, break
        if not found_next:
            break
    
    return distributions

def main(n):
    """
    Main function to calculate permutation distributions.
    
    Parameters:
    -----------
    n : int
        Maximum number of digits to calculate
    """
    for i in range(n):
        start = time.time()
        dist = generate_digit_distributions(i)
        end = time.time()
        print(f"Distribution generation for {i}: {end - start:.2f}s")
        
        start = time.time()
        sum1 = 0
        for j in range(len(dist)):
            
            sum1 += len_of_permutations(dict_to_list(dist[j]), dist[j])
        end = time.time()
        
        print(f"Time taken for {i} is {end - start:.2f}s")
        print(f"Number of permutations for {i} is {sum1}")
        last = sum1

if __name__ == "__main__":
    main(5)  # Adjust the number as needed