import bst


def find_branch_sum(root):
    sum_list = []
    sum=0
    return find_branch_sum_helper(root,sum_list,sum)
     
def find_branch_sum_helper(root,sum_list,sum):
    sum += root.data
    
    if root.left:
        sum = find_branch_sum_helper(root.left,sum_list,sum)
    
    if root.right:
        sum = find_branch_sum_helper(root.right,sum_list,sum)
    
    
    if (not root.right) and (not root.left):
        sum_list.append(sum)
        
    