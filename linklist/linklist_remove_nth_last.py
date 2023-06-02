"""Find all permutations of an array
"""

arr = [1, 2, 3]


def get_permutation(array):
    permutations = []
    get_permutation_helper(array, [], permutations)
    return permutations


def get_permutation_helper(array, currentPermutation, permutations):
    if not len(array) and len(currentPermutation):
        permutations.append(currentPermutation)
    for i in range(len(array)):
        newArray = array[:i] + array[i + 1 :]
        newPermutation = currentPermutation + [array[i]]
        get_permutation_helper(newArray, newPermutation, permutations)
