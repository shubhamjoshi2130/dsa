# Given an array of integers where each number represents the number of jumps
# If positive jump forward if -ve jump backward
# we need to check if we start from first index we end at last index

arr = [2, 3, 1, -4, -4, 2]


def single_cycle_check(arr):
    curentIdx = 0
    numElementsVisited = 0
    while numElementsVisited < len(arr):
        if numElementsVisited > 0 and curentIdx == 0:
            return False
        numElementsVisited += 1
        curentIdx = getNextIdx(curentIdx, arr)
    return curentIdx == 0


def getNextIdx(curentIdx, arr):
    jump = arr[curentIdx]
    nextIdx = (curentIdx + jump) % len(arr)
    return nextIdx if nextIdx >= 0 else nextIdx + len(arr)
