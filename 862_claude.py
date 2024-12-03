# from itertools import permutations
# from collections import Counter

# def count_larger_permutations(num):
#     """
#     Efficiently count larger permutations without generating all of them.
#     """
#     # Convert number to list of digits
#     digits = list(str(num))
#     digit_counter = Counter(digits)
    
#     # Total permutations possible
#     total_perms = factorial(len(digits)) // reduce_factorial(digit_counter)
    
#     # Count permutations larger than original number
#     larger_count = 0
#     for perm in permutations(digits):
#         # Skip leading zero permutations
#         if perm[0] == '0':
#             continue
        
#         # Convert to integer and compare
#         perm_num = int(''.join(perm))
#         if perm_num > num:
#             larger_count += 1
    
#     return larger_count

# def S(k):
#     """
#     Optimized calculation of S(k)
#     """
#     return sum(count_larger_permutations(n) for n in range(10**(k-1), 10**k))

# # Helper functions for factorial calculations
# from functools import reduce
# from math import factorial

# def reduce_factorial(counter):
#     """
#     Calculate factorial reduction for repeated digits
#     """
#     denominator = 1
#     for count in counter.values():
#         denominator *= factorial(count)
#     return denominator

# # Solve for S(12)
# result = S(12)
# print(f"S(12) = {result}")


from math import factorial

# Precompute factorials
def precompute_factorials(max_digits):
    fact = [1] * (max_digits + 1)
    for i in range(2, max_digits + 1):
        fact[i] = fact[i - 1] * i
    return fact

# Calculate the number of unique permutations for a given digit distribution
def unique_permutations(digit_counts, total_digits, factorials):
    total_perms = factorials[total_digits]
    for count in digit_counts.values():
        total_perms //= factorials[count]
    return total_perms

# Exclude permutations with leading zeros
def exclude_leading_zeros(digit_counts, total_digits, factorials):
    if 0 not in digit_counts:
        return 0
    # Reduce digit count for 0 and calculate permutations
    digit_counts[0] -= 1
    perms_with_zero = unique_permutations(digit_counts, total_digits - 1, factorials)
    digit_counts[0] += 1
    return perms_with_zero

# Calculate T(n) for a given digit distribution
def calculate_tn(digit_counts, total_digits, factorials):
    total_perms = unique_permutations(digit_counts, total_digits, factorials)
    zero_exclusions = exclude_leading_zeros(digit_counts, total_digits, factorials)
    return total_perms - zero_exclusions

# Generate all possible digit distributions for a given number of digits
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

# Calculate S(k)
def calculate_sk(k, factorials):
    digit_distributions = generate_digit_distributions(k)
    print(digit_distributions)
    sk = 0
    for dist in digit_distributions:
        sk += calculate_tn(dist, k, factorials)
    return sk

# Main logic
def main():
    max_digits = 12
    factorials = precompute_factorials(max_digits)
    result = calculate_sk(12, factorials)
    print("S(12):", result)

# Run the program
main()