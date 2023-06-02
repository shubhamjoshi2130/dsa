class Node:
    def __init__(self, data):
        self.children = []
        self.data = data

    def addChild(self, data):
        self.children.append(Node(data))

    # O(v + e) time | O(v) space
    def breadthFirstSearch(self, array):
        sum_lst=[self.data]
        queue = [current.children]
        
        while len(queue) > 0:
            current = queue.pop(0)
            level_lst = []
            sum_level = 0
            for nodes in current:
                sum_level += nodes.data
                level_lst.extend(nodes.children)
            queue.append(level_lst)
            sum_lst.append(sum_level)
        return array
