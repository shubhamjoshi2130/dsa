# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def closestNodes(self, root: Optional[TreeNode], queries: List[int]) -> List[List[int]]:
        
        
        result_list = []
        

        for num in queries:
            root_t_min = root
            root_t_max = root
            clo_diff_min = float('-inf')
            clo_diff_max = float('inf')
            min_val = -1
            max_val = -1
            while ((root_t_min!=None) & (root_t_max!=None)):
                if root_t_min:
                    new_coll_diff_min = num - root_t_min.val
                    # print("num:",num)
                    # print("new_coll_diff_min:",new_coll_diff_min)
                    if (new_coll_diff_min == 0):
                        min_val = root_t_min.val
                        root_t_min = None
                    elif (new_coll_diff_min > clo_diff_min) & (new_coll_diff_min <= 0):
                        # print("!! inside")
                        clo_diff_min = new_coll_diff_min
                        min_val = root_t_min.val
                        root_t_min = root_t_min.left
                    elif (new_coll_diff_min > 0):
                        root_t_min = root_t_min.right

                if root_t_max:
                    new_coll_diff_max = num - root_t_max.val
                    if (new_coll_diff_max == 0):
                        max_val = root_t_max.val
                        root_t_max = None
                    elif (new_coll_diff_max < clo_diff_max) & (new_coll_diff_max >= 0):
                        clo_diff_max = new_coll_diff_max
                        max_val = root_t_max.val
                        root_t_max = root_t_max.right
                    elif (new_coll_diff_max < 0):
                        root_t_max = root_t_max.left 
                        
            result_list.append([max_val,min_val])
        return result_list