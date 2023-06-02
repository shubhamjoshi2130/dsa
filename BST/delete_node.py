import bst


def delete_node(root,number):
    delete_node_helper(root,number)
     
def delete_node_helper(root,number):
    is_left = True
    if root.data > number:
        if root.left:
            node_to_del = delete_node_helper(root.left,number)
        else:
            return None
    elif root.data < number:
        if root.right:
            node_to_del = delete_node_helper(root.right,number)
            is_left = False
        else:
            return None
    else:
        return root
    
    if node_to_del:
        if node_to_del.left:
            max_node=find_max(node_to_del,number)
            node_to_del.data = max_node.data
            delete_node_helper(node_to_del.left,max_node.data)
        elif node_to_del.right:
            min_node=find_min(node_to_del,number)
            node_to_del.data = min_node.data
            delete_node_helper(node_to_del.right,min_node.data)
        else:
            if is_left:
                root.left = None
            else:
                root.right = None         
    return None