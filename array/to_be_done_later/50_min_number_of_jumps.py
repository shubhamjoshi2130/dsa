# min number of jumps required to go from 1st to last index

arr = [3,4,2,1,2,3,7,1,1,1,3]

def min_jumps(arr_in):
    jumps=[0] + [float("inf") for _ in arr_in[1:]]
    min_jumps_helper(arr_in,jumps,1,1)
    return jumps[-1]

def min_jumps_helper(arr_in,jumps,i,j):
    for i in range(len(jumps)):
        for j in range(i):
            if (arr_in[j] + j) >= i:
                jumps[i] = min(jumps[i],jumps[j] + 1)
    
    