"""
Note: Chapter 2 is a harder version of this puzzle.
You're trying to open a lock. The lock comes with a wheel which has the integers from 11 to NN arranged in a circle in order around it (with integers 11 and NN adjacent to one another). The wheel is initially pointing at 11.
For example, the following depicts the lock for N = 10N=10 (as is presented in the second sample case).

It takes 11 second to rotate the wheel by 11 unit to an adjacent integer in either direction, and it takes no time to select an integer once the wheel is pointing at it.
The lock will open if you enter a certain code. The code consists of a sequence of MM integers, the iith of which is C_iC 
i
​
 . Determine the minimum number of seconds required to select all MM of the code's integers in order.
Please take care to write a solution which runs within the time limit.
Constraints
3 \le N \le 50{,}000{,}0003≤N≤50,000,000
1 \le M \le 1{,}0001≤M≤1,000
1 \le C_i \le N1≤C 
i
​
 ≤N
Sample test case #1
N = 3
M = 3
C = [1, 2, 3]
Expected Return Value = 2
Sample test case #2
N = 10
M = 4
C = [9, 4, 4, 8]
Expected Return Value = 11
Sample Explanation
"""
from typing import List
# Write any import statements here

def getMinCodeEntryTime(N: int, M: int, C: List[int]) -> int:
  # Write your code here
  
  pointer = 1
  total_time = 0
  
  for i in range(M):
    rotate = abs(C[i] - pointer)
    seconds = min(rotate,(N-rotate))
    total_time += seconds
    pointer = C[i]
  return total_time
