from math import factorial
cimport cython

@cython.boundscheck(False)  # Turn off bounds checking for performance
@cython.wraparound(False)   # Turn off negative index checking
def len_of_permutations(list1):
    """
    Calculate number of unique permutations excluding those starting with 0.
    """
    cdef int total_perms = factorial(len(list1))
    cdef dict digit_counts = {}
    cdef int digit, count, zero_perms

    # Count occurrences of each digit
    for digit in list1:
        if digit in digit_counts:
            digit_counts[digit] += 1
        else:
            digit_counts[digit] = 1

    # Divide total permutations by repeated digit factorials
    for count in digit_counts.values():
        total_perms //= factorial(count)

    # Calculate leading zero permutations
    zero_perms = 0
    if 0 in digit_counts and list1[0] == 0:
        zero_perms = factorial(len(list1) - 1)
        zero_digit_counts = {k: v for k, v in digit_counts.items() if k != 0}
        for count in zero_digit_counts.values():
            zero_perms //= factorial(count)

    total_perms -= zero_perms

    return sum(range(total_perms))