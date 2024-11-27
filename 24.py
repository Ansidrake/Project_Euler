'''

get permutations of the number

'''


list1 = [0,1,2,3,4,5,6,7,8,9]

permutations = []

# def get_permutations(list1):
#     permutations = []
#     for i in range(len(list1)):
#         for j in range(len(list1)):
#             for k in range(len(list1)):
#                 if i == j or i == k or j == k:
#                     continue
#                 permutations.append([list1[i],list1[j],list1[k]])  
#     return permutations



def get_permutations2(list1): 
    '''
    This function generates all permutations of a given list of elements.
    
    The function works by selecting each element of the list in turn, and then
    recursively generating all permutations of the remaining elements. The
    base case for the recursion is when the list has only one element, in which
    case the only permutation is the list itself.
    
    The outer loop iterates over the elements of the list. For each element, it
    generates all permutations of the remaining elements by calling itself
    recursively. The inner loop then iterates over the permutations of the
    remaining elements, and for each permutation, it inserts the current element
    at the start of the permutation, and adds the new permutation to the list
    of all permutations.
    
    For example, if the list is [1,2,3], the outer loop will select each of
    the elements in turn, and then recursively generate all permutations of
    the remaining elements. When the element is 1, the remaining elements are
    [2,3], and the permutations of these are [[2,3],[3,2]]. The inner loop
    will then insert the element 1 at the start of each permutation, to give
    [[1,2,3],[1,3,2]]. The same process is then repeated for the elements 2
    and 3, to give [[2,1,3],[2,3,1],[3,1,2],[3,2,1]].
    
    The function returns the list of all permutations.
    '''
    if len(list1) == 1:
        return [list1]
    permutations = []
    for i in range(len(list1)):
        for j in get_permutations2(list1[:i] + list1[i+1:]):
            permutations.append([list1[i]] + j)
    return permutations

import itertools

def get_permutations3(list1):
    return list(itertools.permutations(list1))

x = get_permutations3(list1)
y = get_permutations2(list1)

print(len(x))
print(len(y))

answer = [2,7,8,3,9,1,5,4,6,0]

print(x[999999])
# print(y[1000001])
# y = sorted(y)
# print(y[1000001])
# print(y.index(answer))

