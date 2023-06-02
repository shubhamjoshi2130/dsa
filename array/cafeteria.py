    """A cafeteria table consists of a row of NN seats, numbered from 11 to NN from left to right. Social distancing guidelines require that every diner be seated such that KK seats to their left and KK seats to their right (or all the remaining seats to that side if there are fewer than KK) remain empty.
There are currently MM diners seated at the table, the iith of whom is in seat S_iS 
i
​
 . No two diners are sitting in the same seat, and the social distancing guidelines are satisfied.
Determine the maximum number of additional diners who can potentially sit at the table without social distancing guidelines being violated for any new or existing diners, assuming that the existing diners cannot move and that the additional diners will cooperate to maximize how many of them can sit down.
Please take care to write a solution which runs within the time limit.
Constraints
1 \le N \le 10^{15}1≤N≤10 
15
 
1 \le K \le N1≤K≤N
1 \le M \le 500{,}0001≤M≤500,000
M \le NM≤N
1 \le S_i \le N1≤S 
i
​
 ≤N
Sample test case #1
N = 10
K = 1
M = 2
S = [2, 6]
Expected Return Value = 3
    """

from typing import List
# Write any import statements here

def getMaxAdditionalDinersCount(N: int, K: int, M: int, S: List[int]) -> int:
  # Write your code here
  seating_dict = {x:False for x in range(N)}
  for i in S:
    seating_dict[i] = True
  print(f"********** dict : {seating_dict}")  
  total = 0
  for i in S:
    left_count = i
    total_left_count = 0
    total_right_count = 0
    right_count = i
    start_pt = i
    total_old = total
    total = 0
    while left_count >= 0:
      if ((start_pt-left_count)%(K + 1)==0) and (not seating_dict[left_count]):
        print(f"********** inside : {(start_pt-left_count)}")
        seating_dict[left_count] = True
        total_left_count += 1
        print(f"********** inside : {(start_pt-total_left_count)}")
      elif ((start_pt-left_count)%(K + 1)!=0) and seating_dict[left_count]:
        print(f"********** inside2 : {(start_pt-left_count)}")
        total_left_count -= 1
        start_pt = left_count
      left_count -= 1
      
    start_pt = i  
    while right_count < N:
      if ((right_count - start_pt)%(K + 1)==0) and (not seating_dict[right_count]):
        seating_dict[right_count] = True
        total_right_count += 1
      elif ((right_count - start_pt)%(K + 1)!=0) and seating_dict[right_count]:
        total_right_count += 1
        start_pt = right_count
      right_count += 1
      
    print(f"********** total_right_count : {total_right_count}")
    print(f"********** total_left_count : {total_left_count}")
    total = total_right_count + total_left_count
    total = max(total_old,total)  
  return total
